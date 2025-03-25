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
        user_input = input("\nNidhi: ")
        
        # Check if user wants to exit
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Nidhi: Goodbye! Have a great day!")
            break
        
        # Get response from the agent
        response = agent.prompt(user_input)
        
        # Print the response
        print(f"Metis Agent: {response}")

if __name__ == "__main__":
    main()
