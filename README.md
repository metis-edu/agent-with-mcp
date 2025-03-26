# Simple AI Agent with MCP, Alith and UV

This project demonstrates how to create a simple AI agent using Alith, MCP (Model Context Protocol), and UV to fetch and provide block numbers from the Metis Blockchain (L2).

## What is MCP?

MCP (Model Context Protocol) is a powerful protocol that enables an AI agent to integrate with external tools or services in a context-aware manner. This allows the creation of AI agents that can perform complex operations by interacting with external APIs or systems. With MCP, an AI agent can access and manipulate external data seamlessly.

## What is UV?

UV is a lightweight, user-friendly, and flexible Python tool designed to manage virtual environments, dependencies, and projects in a streamlined way. It enables you to easily set up and manage your Python projects without requiring complex tools like pipenv or virtualenv.

For detailed installation and usage instructions, check out the UV Documentation.

## Prerequisites

Before starting the project, ensure you have UV installed. UV manages Python environments and dependencies.

### Install UV:

1. For macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. For Windows, follow the installation instructions on the UV website.

### Verify UV Installation:

After installation, verify it by running:
```bash
uv --help
```

## Setup Instructions

### 1. Create a New Project Directory

Create a new project directory and initialize it with UV:
```bash
mkdir my_mcp_project
cd my_mcp_project
uv init
```

Create and activate the virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
```

### 2. Install Required Packages

Install the required packages, including Alith, Web3, MCP, and requests using UV:
```bash
uv pip install alith web3 requests
```

```bash
uv add "mcp[cli]"
```

### 3. Create the MCP Server

Create a file named `mcp_server.py` with the following code:
```python
from mcp.server.fastmcp import FastMCP
from web3 import Web3

# Initialize the MCP server
mcp = FastMCP("MetisBlockServer")

# Connect to Metis mainnet
w3 = Web3(Web3.HTTPProvider("https://andromeda.metis.io/?owner=1088"))

# MCP Tool: Fetch Latest Block Number (already working)
@mcp.tool()
def get_latest_block() -> int:
    """Fetches the latest block number from Metis mainnet."""
    return w3.eth.block_number

# MCP Tool: Fetch Previous Block Number (already working)
@mcp.tool()
def get_previous_block() -> int:
    """Fetches the previous block number from Metis mainnet."""
    latest_block = get_latest_block()      
    return latest_block - 1

# Run the MCP server
if __name__ == "__main__":
    latest_block = get_latest_block()
    previous_block = get_previous_block()

    print(f"Latest Block Number: {latest_block}")
    print(f"Previous Block Number: {previous_block}")

    mcp.run()
```

### 4. Create the AI Agent Code

Create a file named `main.py`:
```python
from alith import Agent
import os

agent = Agent(
    name="MetisBlockAgent",
    model="gpt-4o-mini",
    preamble="You are an assistant that provides Metis blockchain block numbers.",
    mcp_config_path="server_config.json"
)

def main():
    print("🤖 Simple Metis AI Agent is running. Type 'exit' to quit.")
    print("Ask me anything about Metis L2 or blockchain!")
    
    while True:
        # Get user input
        user_input = input("\nUSER: ")
        
        # Check if user wants to exit
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("USER: Goodbye! Have a great day!")
            break
        
        # Get response from the agent
        response = agent.prompt(user_input)
        
        # Print the response
        print(f"Metis Agent: {response}")

if __name__ == "__main__":
    main()
```

### 5. Create the Server Configuration File

Create a `server_config.json` file:
```json
{
    "mcpServers": {
        "blockchain": {
            "command": "python",
            "args": [
                "mcp_server.py"
            ]
        }
    }
}
```

## Running the Project

### Step 1: Run the MCP Server

Run the MCP server:
```bash
python3 mcp_server.py
```
This will start the MCP server and print out the latest and previous block numbers.

### Step 2: Run the AI Agent

In a separate terminal window, run the AI Agent:
```bash
python3 main.py
```

## Expected Output

When you run `main.py`, you will be prompted with:
```
🤖 Simple Metis AI Agent is running. Type 'exit' to quit.
Ask me anything about Metis L2 or blockchain!

USER: What is the latest Metis block number?
Metis Agent: The latest Metis block number is 20010305.

USER: What was the previous block number?
Metis Agent: The previous Metis block number is 20010304.
```

To exit the program, type exit, quit, or bye.

## Project Structure

```
my_mcp_project/
├── .venv/                  # Virtual environment
├── .gitignore
├── .python-version
├── main.py                 # Alith AI agent implementation
├── mcp_server.py           # MCP server implementation
├── server_config.json      # Configuration file for the Alith agent
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── uv.lock
```

## Conclusion

By following these steps, you have created a simple AI agent that fetches block numbers from the Metis blockchain using MCP and Alith. You can now interact with the agent and ask about the latest and previous block numbers, and the agent will return the data based on real-time queries from the blockchain.
