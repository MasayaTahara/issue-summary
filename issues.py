from github.PaginatedList import PaginatedList


SECURITYHUB_CRITICAL_LABELS = 'securityhub/CRITICAL'
SECURITYHUB_HIGH_LABELS = 'securityhub/HIGH'
SECURITYHUB_MEDIUM_LABELS = 'securityhub/MEDIUM'
SECURITYHUB_INPROGRESS_LABELS = 'WIP'
SECURITYHUB_INREVIEW_LABELS = 'inreview'


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


def count_inprogress_issues(issues: PaginatedList):
    count_critical = 0
    count_high = 0
    count_medium = 0
    for issue in issues:
        if SECURITYHUB_INPROGRESS_LABELS in [labels.name for labels in issue.labels]:
            for label in issue.labels:
                if SECURITYHUB_CRITICAL_LABELS == label.name:
                    count_critical += 1
                elif SECURITYHUB_HIGH_LABELS == label.name:
                    count_high += 1
                if SECURITYHUB_MEDIUM_LABELS == label.name:
                    count_medium += 1
    return [count_critical, count_high, count_medium]

def count_inreview_issues(issues: PaginatedList):
    count_critical = 0
    count_high = 0
    count_medium = 0
    for issue in issues:
        if SECURITYHUB_INREVIEW_LABELS in [labels.name for labels in issue.labels]:
            for label in issue.labels:
                if SECURITYHUB_CRITICAL_LABELS == label.name:
                    count_critical += 1
                elif SECURITYHUB_HIGH_LABELS == label.name:
                    count_high += 1
                if SECURITYHUB_MEDIUM_LABELS == label.name:
                    count_medium += 1
    return [count_critical, count_high, count_medium]
