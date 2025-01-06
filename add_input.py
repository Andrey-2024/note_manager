# add_input.py
#@title
username = input("Enter your username: ")
title = input("Enter the title of your note: ")
content = input("Enter the content of your note: ")
status = input("Enter the status of your note (e.g., Draft, Published): ")
created_date = input("Enter the created date (YYYY-MM-DD): ")
issue_date = input("Enter the issue date (YYYY-MM-DD): ")

print(f"Username: {username}")
print(f"Title: {title}")
print(f"Content: {content}")
print(f"Status: {status}")
print(f"Created Date: {created_date}")
print(f"Issue Date: {issue_date}")
