from labka import Bug, Backlog

def main():
    bug1 = Bug("UI issue", "Minor", "2023-11-01", "OPEN", "Developer1")
    bug2 = Bug("Critical functionality bug", "Critical", "2023-10-30", "RESOLVED", "Developer2")
    bug3 = Bug("Performance problem", "Major", "2023-11-05", "RESOLVED", "Developer1")
    bug4 = Bug("Database error", "Major", "2023-11-10", "OPEN", "Developer3")

    backlog = Backlog()
    backlog.add_bug(bug1)
    backlog.add_bug(bug2)
    backlog.add_bug(bug3)
    backlog.add_bug(bug4)

    backlog.get_resolved_bugs_for_assignee("Developer1")
    backlog.sort_by_severity()


if __name__ == "__main__":
    main()
