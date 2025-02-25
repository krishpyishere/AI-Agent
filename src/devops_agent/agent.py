from __future__ import annotations
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from enum import Enum
import hashlib
from pathlib import Path
import subprocess
import logging
from .exceptions import ValidationError, AuthenticationError
from .auth import AuthManager

class ScriptType(Enum):
    BASH = "bash"
    PYTHON = "python"
    POWERSHELL = "powershell"

class DevOpsAutomationAgent:
    def __init__(self, storage_path: str = "automations_db.json", auth_required: bool = True):
        self.storage_path = storage_path
        self.auth_manager = AuthManager()
        self.auth_required = auth_required
        self.automations_db = self._load_database()
        self._setup_logging()

    def _setup_logging(self) -> None:
        """Set up logging configuration."""
        logging.basicConfig(
            filename='devops_agent.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def _load_database(self) -> Dict[str, Any]:
        """Load existing automations from JSON file or create new database."""
        if os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {"automations": [], "versions": {}}
        return {"automations": [], "versions": {}}

    def _save_database(self) -> None:
        """Save automations to JSON file."""
        with open(self.storage_path, 'w', encoding='utf-8') as f:
            json.dump(self.automations_db, f, indent=2)

    def _validate_script(self, script: str, script_type: ScriptType) -> bool:
        """Basic validation of scripts."""
        if not script.strip():
            raise ValidationError("Script cannot be empty")
        
        if script_type == ScriptType.PYTHON:
            try:
                compile(script, '<string>', 'exec')
            except SyntaxError as e:
                raise ValidationError(f"Invalid Python syntax: {str(e)}")
        
        return True

    def add_automation(self, 
                      question: str, 
                      script: str, 
                      tags: List[str], 
                      script_type: ScriptType,
                      user_id: str) -> Dict[str, Any]:
        """Add new automation script with associated question and tags."""
        if self.auth_required and not self.auth_manager.is_authorized(user_id):
            raise AuthenticationError("User not authorized")

        self._validate_script(script, script_type)
        
        script_hash = hashlib.sha256(script.encode()).hexdigest()
        
        automation = {
            "id": len(self.automations_db["automations"]) + 1,
            "question": question,
            "script": script,
            "script_type": script_type.value,
            "tags": tags,
            "created_at": datetime.now().isoformat(),
            "created_by": user_id,
            "times_used": 0,
            "version": 1,
            "script_hash": script_hash
        }
        
        self.automations_db["automations"].append(automation)
        self.automations_db["versions"][str(automation["id"])] = [{
            "version": 1,
            "script": script,
            "script_hash": script_hash,
            "modified_at": datetime.now().isoformat(),
            "modified_by": user_id
        }]
        
        self._save_database()
        self.logger.info(f"New automation added: ID {automation['id']}")
        return automation

    def search_automation(self, query: str) -> List[Dict[str, Any]]:
        """Search for automations based on question or tags."""
        results = []
        query = query.lower()
        
        for automation in self.automations_db["automations"]:
            if (query in automation["question"].lower() or 
                any(query in tag.lower() for tag in automation["tags"])):
                results.append(automation)
        
        return results

    def get_automation(self, automation_id: int) -> Optional[Dict[str, Any]]:
        """Retrieve specific automation by ID."""
        for automation in self.automations_db["automations"]:
            if automation["id"] == automation_id:
                automation["times_used"] += 1
                self._save_database()
                return automation
        return None

    def execute_automation(self, 
                         automation_id: int, 
                         user_id: str, 
                         params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute an automation script."""
        if self.auth_required and not self.auth_manager.is_authorized(user_id):
            raise AuthenticationError("User not authorized")

        automation = self.get_automation(automation_id)
        if not automation:
            raise ValueError(f"Automation with ID {automation_id} not found")

        script_type = ScriptType(automation["script_type"])
        script = automation["script"]

        try:
            if script_type == ScriptType.PYTHON:
                # Execute Python script with parameters
                local_vars: Dict[str, Any] = {}
                if params:
                    script = f"params = {params}\n" + script
                exec(script, {}, local_vars)
                result = local_vars.get('result', None)
            else:
                # Execute shell scripts
                result = subprocess.run(
                    script, 
                    shell=True, 
                    capture_output=True, 
                    text=True
                )
                
            self.logger.info(f"Automation {automation_id} executed successfully")
            return {
                "success": True,
                "result": result,
                "automation_id": automation_id
            }
            
        except Exception as e:
            self.logger.error(f"Error executing automation {automation_id}: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "automation_id": automation_id
            } 