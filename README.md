# DevOps Automation Agent

A Python-based automation agent designed to manage, store, and execute DevOps tasks efficiently. This tool provides version control, authentication, and execution capabilities for various types of automation scripts.

## Features

- 🔐 Authentication and authorization system
- 📝 Script version control
- 🔍 Search functionality with tagging
- 🚀 Multiple script type support (Python, Bash, PowerShell)
- 📊 Usage tracking and logging
- ✅ Script validation
- 🔄 Parameter support for script execution

## Installation

1. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install the required packages:
```bash
python3 -m pip install -r requirements.txt
```

3. If requirements.txt is not present, install the core dependencies:
```bash
python3 -m pip install python-dotenv
python3 -m pip install fastapi
python3 -m pip install uvicorn
```

## Running the Script

### Initial Setup

1. Clone or download the project to your local machine:

### Test Installation

Create a test script `test_agent.py` in your project root:

```python
from devops_agent.agent import DevOpsAutomationAgent, ScriptType

def test_basic_functionality():
    # Initialize the agent with authentication disabled for testing
    agent = DevOpsAutomationAgent(
        storage_path="test_automations.json",
        auth_required=False
    )

    # Add a simple test automation
    test_automation = agent.add_automation(
        question="Test disk space check",
        script="df -h",
        tags=["test", "system"],
        script_type=ScriptType.BASH,
        user_id="test_user"
    )

    print("✅ Successfully added automation")

    # Search for the automation
    search_results = agent.search_automation("disk")
    print(f"🔍 Found {len(search_results)} matching automation(s)")

    # Execute the automation
    result = agent.execute_automation(
        automation_id=test_automation["id"],
        user_id="test_user"
    )
    print("🚀 Execution result:", result)

if __name__ == "__main__":
    test_basic_functionality()
```

Run the test script:
```bash
python3 test_agent.py
```

If everything is set up correctly, you should see output showing the successful addition, search, and execution of a test automation.

## Getting Started

After completing the initial setup:

1. Create a new `.env` file in the root directory using `.env.example` as a template
2. Add executable permissions to the scripts:
   ```bash
   chmod +x scripts/*.sh
   ```
3. Run the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   # or
   pnpm dev
   ```
4. Open [http://localhost:3000](http://localhost:3000) in your browser to see the application

## Usage

### Basic Example

```python
from devops_agent.agent import DevOpsAutomationAgent, ScriptType

# Initialize the agent
agent = DevOpsAutomationAgent(storage_path="automations_db.json")

# Add a new automation
automation = agent.add_automation(
    question="How to check disk space?",
    script="df -h",
    tags=["system", "disk", "storage"],
    script_type=ScriptType.BASH,
    user_id="user123"
)

# Execute the automation
result = agent.execute_automation(
    automation_id=automation["id"],
    user_id="user123"
)

# Search for automations
results = agent.search_automation("disk")
```

### Supported Script Types
- BASH
- PYTHON
- POWERSHELL

### Authentication
By default, authentication is required. You can disable it by setting `auth_required=False`:
```python
agent = DevOpsAutomationAgent(auth_required=False)
```

### Parameters
When executing Python scripts, you can pass parameters:
```python
result = agent.execute_automation(
    automation_id=1,
    user_id="user123",
    params={"path": "/home", "limit": 100}
)
```

## AI Integration

The DevOps Automation Agent can be integrated with AI models to:

1. **Natural Language Processing**: Search and match automation scripts based on natural language queries
2. **Script Generation**: Generate automation scripts based on user requirements
3. **Parameter Suggestions**: Recommend parameters based on script analysis

### Example with AI Integration

```python
from devops_agent.agent import DevOpsAutomationAgent
from your_ai_module import AIHandler  # You'll need to implement this

# Initialize the agent with AI capabilities
agent = DevOpsAutomationAgent(storage_path="automations_db.json")
ai_handler = AIHandler()

# Search using natural language
query = "Show me all scripts that help with Docker container management"
results = agent.search_automation(query)

# Generate a new script using AI
script_request = "Create a script to cleanup unused Docker images"
suggested_script = ai_handler.generate_script(script_request)

# Add the AI-generated automation
automation = agent.add_automation(
    question=script_request,
    script=suggested_script,
    tags=["docker", "cleanup", "maintenance"],
    script_type=ScriptType.BASH,
    user_id="user123"
)
```

### Planned AI Features
- Script validation and security checking
- Automated tagging of scripts
- Performance optimization suggestions
- Context-aware parameter validation

## Testing

To run the tests, execute:

```bash
# Run all tests
python -m pytest

# Run tests with coverage report
python -m pytest --cov=devops_agent tests/
```

The tests are located in the `tests` directory and include:
- Unit tests for the DevOpsAutomationAgent class
- Test cases for automation creation, search, and execution
- Automatic cleanup of test files