from mcp.server.fastmcp import FastMCP
from web3 import Web3

# Initialize the MCP server
mcp = FastMCP("MetisBlockServer")

# Connect to Metis mainnet
w3 = Web3(Web3.HTTPProvider("https://andromeda.metis.io/?owner=1088"))

# MCP Tool: Fetch Latest Block Number (already working)
@mcp.tool()
def get_latest_block() -> str:
    """Returns the latest block number from Metis mainnet."""
    block = w3.eth.block_number
    return {"message": f"The latest Metis block number is {block}."}

@mcp.tool()
def get_previous_block() -> str:
    """Returns the previous block number."""
    block = w3.eth.block_number - 1
    return {"message": f"The previous Metis block number is {block}."}

# Run the MCP server
if __name__ == "__main__":
    latest_block = get_latest_block()
    previous_block = get_previous_block()

    print(f"Latest Block Number: {latest_block}")
    print(f"Previous Block Number: {previous_block}")

    mcp.run()