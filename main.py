from alith import Agent
import os

agent = Agent(
    name="MetisBlockAgent",
    model="gpt-4o-mini",
    preamble=(
        "You are an assistant that provides Metis blockchain block numbers "
        "and GitHub repository information. "
        "For blockchain-related queries, use tools like get_latest_block or get_previous_block. "
        "For GitHub-related questions about specific repositories (like stars, forks, or description), "
        "use the get_repo_info tool directly with the correct owner and repo name."
    ),
    mcp_config_path="server_config.json"
)

def main():
    print("🤖 Simple Me tis AI Agent is running. Type 'exit' to quit.")
    print("Ask me anything about Metis blocks or GitHub repos!")
    
    while True:
        # Get user input
        user_input = input("\Demo: ")
        
        # Check if user wants to exit
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("User: Goodbye! Have a great day!")
            break
        
        # Get response from the agent
        response = agent.prompt(user_input)
        
        # Print the response
        print(f"Metis Agent: {response}")

if __name__ == "__main__":
    main()
