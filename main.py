from gitlab_api import get_commits, get_commit_diff

def main():
    print("Fetching recent commits...")

    # Example: Fetch last 10 commits
    commits = get_commits(per_page=10)

    for commit in commits:
        print(f"\nCommit: {commit['id'][:7]} - {commit['title']}")
        diffs = get_commit_diff(commit['id'])

        for diff in diffs:
            file_path = diff['new_path']
            print(f" - Modified File: {file_path}")
            # You can later add file-type filter and diff content analysis here
            # e.g., count lines added/deleted etc.

if __name__ == "__main__":
    main()
