#%% public GitHub API 🐙
from github import Github
g = Github()
# #%% private GitHub API 🐙
# from dotenv import load_dotenv
# import os
# load_dotenv()
# token = os.getenv("GITHUB_API_TOKEN")
# if token is None:
#     raise ValueError("GITHUB_API_TOKEN not set in environment or .env file")
# #%%
# # Authenticate with GitHub
# g = Github(token)
#%% Get public repos for a user
username = "yanndebray"
user = g.get_user(username)
repos = user.get_repos()
print("Number of public repos :",len(list(repos)))
print(f"Repos for {username}:")
for repo in repos:
    print(repo.name)

#%% Get info about a specific repo
# repo = user.get_repo("matlab-with-python-book")
repo = g.get_repo("yanndebray/matlab-with-python-book")
print(f"Repo {repo.name} has {repo.stargazers_count} stars and {repo.forks_count} forks")
#%% Get the README
readme = repo.get_readme()
print(readme.decoded_content.decode())
#%% Get the license
license = repo.get_license()
print(license.license.name)
#%% Get the forks
forks = repo.get_forks()
print(f"Repo {repo.name} has {len(list(forks))} forks")
for fork in forks:
    print(fork.full_name)
#%% Get the languages
# https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repository-languages
# Lists languages for the specified repository. 
# The value shown for each language is the number of bytes of code written in that language.
languages = repo.get_languages()
for lang in languages:
    print(lang, int(languages[lang] / 1024), "KB")
#%% Get the tags
tags = repo.get_tags()
print(f"Repo {repo.name} has {len(list(tags))} tags")
for tag in tags:
    print(tag.name)
#%% Get open issues for a repo
issues = repo.get_issues()
print(f"Repo {repo.name} has {len(list(issues))} open issues")
for issue in issues:
    print(issue.title)

#%% Get issues for a repo
issues = repo.get_issues(state="all")
print(f"Repo {repo.name} has {len(list(issues))} issues")
for issue in issues:
    print(issue.title," - ", issue.state)

#%% Get commits for a repo
commits = repo.get_commits()
print(f"Repo {repo.name} has {len(list(commits))} commits")
for commit in commits:
    print(commit.commit.message)
#%% Get GitHub actions/workflows for a repo
# Get all workflows for the repository
workflows = repo.get_workflows()
print(f"Repo {repo.name} has {workflows.totalCount} workflows.")

for workflow in workflows:
    print("Workflow name:", workflow.name)
    print("Workflow path:", workflow.path)

#%% Get the latest run for a workflow
latest_run = workflows[1].get_runs().get_page(0)[0]
print("Latest run id:", latest_run.id)
print("Latest run status:", latest_run.status)
print("Latest run conclusion:", latest_run.conclusion)
print("Latest run created at:", latest_run.created_at)
print("Latest run updated at:", latest_run.updated_at)
print("Latest run duration:", latest_run.updated_at - latest_run.created_at)
print("Latest run head sha:", latest_run.head_sha)
print("Latest run run number:", latest_run.run_number)
print("Latest run event:", latest_run.event)
print("Latest run workflow id:", latest_run.workflow_id)
print("Latest run workflow url:", latest_run.workflow_url)
print("Latest run html url:", latest_run.html_url)

#%% Get a workflow based on its yml file
repo = g.get_repo("yanndebray/programming-GPTs")
workflow = repo.get_workflow("podcast.yml")
print("Workflow name:", workflow.name)
#%% Get the artifacts for a workflow run
workflow_run = workflow.get_runs().get_page(0)[1]
artifacts = workflow_run.get_artifacts()
print(f"Workflow run {workflow_run.run_number} ({workflow_run.id}) has {len(list(artifacts))} artifacts.")
for artifact in artifacts:
    print("Artifact name:", artifact.name)
    print("Artifact size in bytes:", artifact.size_in_bytes)
    print("Artifact URL:", artifact.archive_download_url)