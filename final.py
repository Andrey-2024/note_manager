# final.py
#@title
note = {
    "username": input("Enter your username: "),
    "content": input("Enter the content of your note: "),
    "status": input("Enter the status of your note: "),
    "created_date": input("Enter the created date (YYYY-MM-DD): "),
    "issue_date": input("Enter the issue date (YYYY-MM-DD): "),
    "titles": [input("Enter title 1: "), input("Enter title 2: "), input("Enter title 3: ")]
}

print("\nNote Details:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
