# add_list.py
#@title
titles = []
for i in range(3):
    title = input(f"Enter title {i + 1}: ")
    titles.append(title)

print("Titles:")
for t in titles:
    print(f"- {t}")
