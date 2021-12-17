import os
from dotenv import load_dotenv
from github import Github

import repo as rep
import issues

load_dotenv()
TOKEN = os.environ['TOKEN']
ORGANIZATION = os.environ['ORGANIZATION']
REPOSITRY = os.environ['REPOSITRY']


if __name__ == '__main__':
    g = Github(TOKEN)
    repo = rep.get_repo(g, ORGANIZATION, REPOSITRY)
    print(repo)

    open_issues = rep.get_issues(repo, state='open')
    counted_open_issues = issues.count_issues(open_issues)
    print('Open issues: [CRITICAL, HIGH, MEDIUM] = {}'.format(
        counted_open_issues))

    counted_inprogress_issues = issues.count_inprogress_issues(open_issues)
    print('In progress issues: [CRITICAL, HIGH, MEDIUM] = {}'.format(
        counted_inprogress_issues))

    counted_inreview_issues = issues.count_inreview_issues(open_issues)
    print('In review issues: [CRITICAL, HIGH, MEDIUM] = {}'.format(
        counted_inreview_issues))

    closed_issues = rep.get_issues(repo, state='closed')
    counted_closed_issues = issues.count_issues(closed_issues)
    print('Closed issues: [CRITICAL, HIGH, MEDIUM] = {}'.format(
        counted_closed_issues))
