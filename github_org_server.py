from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("GitHubOrgServer")

GITHUB_API = "https://api.github.com/orgs/"

@mcp.tool()
def list_org_repos(org_name: str) -> list:
    """Returns a list of public repo names for a GitHub organization."""
    url = f"{GITHUB_API}{org_name}/repos"
    response = requests.get(url)
    
    if response.status_code != 200:
        return ["Error fetching data"]
    
    data = response.json()
    return "\n".join([f"- {repo['full_name']}" for repo in data])


@mcp.tool()
def get_repo_stats(owner: str, repo: str) -> dict:
    """Returns stars, forks, and watchers count for a GitHub repo."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": "Repo not found or API error."}
    
    data = response.json()
    return {
        "stars": data.get("stargazers_count", 0),
        "forks": data.get("forks_count", 0),
        "watchers": data.get("subscribers_count", 0),
        "message": f"⭐ {repo} has {data.get('stargazers_count', 0)} stars, {data.get('forks_count', 0)} forks, and {data.get('subscribers_count', 0)} watchers."
    }

if __name__ == "__main__":
    print("📦 GitHub Org Server running...")
    mcp.run()