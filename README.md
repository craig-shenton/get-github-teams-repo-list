# get-github-teams-repo-list

GitHub API Query Team Repositories

This Python script allows you to fetch and save all repositories associated with a specific team in your GitHub organization. It handles pagination to ensure that all repositories are retrieved, and saves the repository information to an Excel file for easy reference.

## Prerequisites

- Python 3.x
- requests library (can be installed using pip install requests)
- pandas library (can be installed using pip install pandas)

## Setup

Clone this repository to your local machine:

```bash

git clone https://github.com/your-username/get-github-teams-repo-list.git
```

Navigate to the project directory:

```bash

cd get-github-teams-repo-list
```

Open config.py and update the following variables with your GitHub organisation details:

```python

    ORG_NAME = "your_organization"
    TEAM_NAME = "your_team"
    GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"
```

Replace "your_organisation" with your GitHub organisation name, "your_team" with the specific team you want to fetch repositories from, and "YOUR_GITHUB_TOKEN" with your GitHub personal access token.

## Usage

Run the script using the following command:

```bash
python script.py
```

The script will fetch all repositories associated with the specified team, handle pagination, and save the repository information to an Excel file (your_team_repositories.xlsx).

## Notes

- Ensure that your GitHub personal access token has the necessary permissions to read teams and repositories from the organization.
- For security reasons, do not share your personal access token or include it directly in the script. Consider using environment variables or other secure methods to manage your tokens.
