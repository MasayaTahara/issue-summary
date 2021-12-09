import os
from dotenv import load_dotenv
from github import Github

load_dotenv()
TOKEN = os.environ['TOKEN']
ORGANIZATION = os.environ['ORGANIZATION']
REPOSITRY = os.environ['REPOSITRY']

if __name__ == '__main__':
    g = Github(TOKEN)

    for _repo in g.get_organization(ORGANIZATION).get_repos():
        if _repo.name == REPOSITRY:
            repo = _repo
            break
    print(repo)

    for _issue in repo.get_issues():
        print('  issue name: #{:<4} {}'.format(_issue.number, _issue.title))
