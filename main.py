import os
from dotenv import load_dotenv
from github import Github
from github.PaginatedList import PaginatedList
from github.Repository import Repository

load_dotenv()
TOKEN = os.environ['TOKEN']
ORGANIZATION = os.environ['ORGANIZATION']
REPOSITRY = os.environ['REPOSITRY']

SECURITYHUB_CRITICAL_LABELS = 'securityhub/CRITICAL'
SECURITYHUB_HIGH_LABELS = 'securityhub/HIGH'
SECURITYHUB_MEDIUM_LABELS = 'securityhub/MEDIUM'


def get_repo(g: Github, organization, repository) -> Repository:
    for r in g.get_organization(organization).get_repos():
        if r.name == repository:
            repo = r
            break
    return repo


def get_issues(r: Repository, state='open'):
    issues = r.get_issues(state=state)
    return issues


def count_issues(issues: PaginatedList):
    count_critical = 0
    count_high = 0
    count_medium = 0
    for issue in issues:
        for label in issue.labels:
            if SECURITYHUB_CRITICAL_LABELS == label.name:
                count_critical += 1
            elif SECURITYHUB_HIGH_LABELS == label.name:
                count_high += 1
            if SECURITYHUB_MEDIUM_LABELS == label.name:
                count_medium += 1
    return [count_critical, count_high, count_medium]


if __name__ == '__main__':
    g = Github(TOKEN)
    repo = get_repo(g, ORGANIZATION, REPOSITRY)
    print(repo)

    open_issues = get_issues(repo, state='open')
    counted_open_issues = count_issues(open_issues)
    print('Open issues: {}'.format(counted_open_issues))

    closed_issues = get_issues(repo, state='closed')
    counted_closed_issues = count_issues(closed_issues)
    print('Closed issues: {}'.format(counted_closed_issues))
