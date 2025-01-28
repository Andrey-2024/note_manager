#@title Цикл добавления заголовков
def add_titles():
    print("Введите заголовки заметок (или оставьте пустым для завершения):")
    titles = []
    while True:
        title = input("Введите заголовок: ").strip()
        if not title:
            break
        if title in titles:
            print("Заголовок уже существует. Попробуйте другой.")
            continue
        titles.append(title)
    print("\nЗаголовки заметок:")
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title}")

if __name__ == "__main__":
    add_titles()
