# date_changer.py
#@title
from datetime import datetime

created_date = "2025-01-06"
issue_date = "2025-01-10"

formatted_created_date = datetime.strptime(created_date, "%Y-%m-%d").strftime("%d-%m")
formatted_issue_date = datetime.strptime(issue_date, "%Y-%m-%d").strftime("%d-%m")

print(f"Created Date: {formatted_created_date}")
print(f"Issue Date: {formatted_issue_date}")
