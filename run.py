import requests
import pandas as pd

ORG_NAME = "your_organization"
TEAM_NAME = "your_team"
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"

# Function to fetch all teams for the organization
def get_all_teams():
    teams_url = f"https://api.github.com/orgs/{ORG_NAME}/teams"
    teams = []
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    while teams_url:
        response = requests.get(teams_url, headers=headers)
        if response.status_code == 200:
            teams.extend(response.json())
            if 'rel="next"' in response.headers.get("Link", ""):
                teams_url = response.links["next"]["url"]
            else:
                teams_url = None
        else:
            print(f"Failed to retrieve teams. Status code: {response.status_code}")
            teams_url = None

    return teams

# Function to fetch repositories for a specific team (with pagination)
def get_team_repositories(team_url):
    repositories = []
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    while team_url:
        response = requests.get(team_url, headers=headers)
        if response.status_code == 200:
            repos = response.json()
            repositories.extend(repos)
            if 'rel="next"' in response.headers.get("Link", ""):
                team_url = response.links["next"]["url"]
            else:
                team_url = None
        else:
            print(f"Failed to retrieve repositories. Status code: {response.status_code}")
            team_url = None

    return repositories

# Get all teams for the organization
all_teams = get_all_teams()

# Find the specific team by name
selected_team = next((team for team in all_teams if team["name"] == TEAM_NAME), None)

if selected_team:
    # Get repositories for the selected team
    repos_url = f"{selected_team['url']}/repos"
    repositories = get_team_repositories(repos_url)

    # Process repositories as needed
    for repo in repositories:
        print(f"Repository Name: {repo['name']}")

    # Save repositories to Excel file
    df = pd.DataFrame(repositories)
    excel_path = f"{TEAM_NAME}_repositories.xlsx"
    df.to_excel(excel_path, index=False, engine="openpyxl")
    print(f"Repository information saved to {excel_path}.")
else:
    print(f"Team '{TEAM_NAME}' not found in the organization.")




