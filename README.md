# GitHub API 

Use Python to interact with the GitHub API.

`pip install PyGithub`

## PyGitHub

```python
from github import Github
g = Github()
repo = g.get_repo("yanndebray/matlab-with-python-book")
commits = repo.get_commits()
print(f"Repo {repo.name} has {len(list(commits))} commits")
for commit in commits:
    print(commit.commit.message)
```

## Resources

- [GitHub API v3](https://docs.github.com/en/rest)
- [GitHub API Tutorial - Youtube](https://www.youtube.com/watch?v=-kFyPaHNgXo&ab_channel=Andy%27sTechTutorials)
- [[Tutorial] - How to use GitHub REST API for Beginners - Youtube](https://www.youtube.com/watch?v=OvfLavRD1Os&ab_channel=Andy%27sTechTutorials)
- [github REST API v3 Crash Course with Vanilla Javascript (No dependencies) - Youtube](https://www.youtube.com/watch?v=5QlE6o-iYcE&ab_channel=HusseinNasser)