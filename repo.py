from github import Github
from github.Repository import Repository

def get_repo(g: Github, organization, repository) -> Repository:
    for r in g.get_organization(organization).get_repos():
        if r.name == repository:
            repo = r
            break
    return repo


def get_issues(r: Repository, state: str):
    issues = r.get_issues(state=state)
    return issues
