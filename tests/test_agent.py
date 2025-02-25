import unittest
from devops_agent.agent import DevOpsAutomationAgent, ScriptType
import os
import json

class TestDevOpsAutomationAgent(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test"""
        self.test_storage = "test_automations.json"
        self.agent = DevOpsAutomationAgent(
            storage_path=self.test_storage,
            auth_required=False
        )

    def tearDown(self):
        """Clean up after each test"""
        if os.path.exists(self.test_storage):
            os.remove(self.test_storage)

    def test_add_automation(self):
        """Test adding a new automation"""
        automation = self.agent.add_automation(
            question="Test disk space check",
            script="df -h",
            tags=["test", "system"],
            script_type=ScriptType.BASH,
            user_id="test_user"
        )
        
        self.assertIsNotNone(automation["id"])
        self.assertEqual(automation["question"], "Test disk space check")
        self.assertEqual(automation["script"], "df -h")

    def test_search_automation(self):
        """Test searching for automations"""
        # Add test automation
        self.agent.add_automation(
            question="Test disk space check",
            script="df -h",
            tags=["test", "system"],
            script_type=ScriptType.BASH,
            user_id="test_user"
        )

        # Search for it
        results = self.agent.search_automation("disk")
        self.assertTrue(len(results) > 0)
        self.assertTrue(any("disk" in result["question"].lower() for result in results))

    def test_execute_automation(self):
        """Test executing an automation"""
        # Add test automation
        automation = self.agent.add_automation(
            question="Echo test",
            script="echo 'test successful'",
            tags=["test"],
            script_type=ScriptType.BASH,
            user_id="test_user"
        )

        # Execute it
        result = self.agent.execute_automation(
            automation_id=automation["id"],
            user_id="test_user"
        )
        self.assertIn("test successful", result)

if __name__ == '__main__':
    unittest.main() 