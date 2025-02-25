#!/usr/bin/env python3

from src.devops_agent import DevOpsAutomationAgent, ScriptType, AuthManager

def test_automation():
    # Initialize the agent
    agent = DevOpsAutomationAgent()
    
    # Create a user and get authentication
    auth_manager = AuthManager()
    user = auth_manager.create_user("admin", "secure_password")
    token = auth_manager.generate_token("admin", "secure_password")
    
    # Add a sample automation
    automation = agent.add_automation(
        question="How to check system disk usage?",
        script="""
import shutil
total, used, free = shutil.disk_usage('/')
result = {
    'total': total // (2**30),
    'used': used // (2**30),
    'free': free // (2**30)
}
        """,
        tags=["system", "disk", "monitoring"],
        script_type=ScriptType.PYTHON,
        user_id=token
    )
    
    # Execute the automation
    result = agent.execute_automation(automation["id"], token)
    print("Automation result:", result)
    
    # Search for automations
    search_results = agent.search_automation("disk")
    print("\nSearch results:", search_results)

if __name__ == "__main__":
    test_automation() 