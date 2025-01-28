#@title Несколько Заметок
def multiple_notes():
    notes = []
    print("Добро пожаловать в \"Менеджер заметок\"!")
    while True:
        user = input("Введите имя пользователя: ").strip()
        title = input("Введите заголовок заметки: ").strip()
        description = input("Введите описание заметки: ").strip()
        status = input("Введите статус заметки (новая, в процессе, выполнено): ").strip()
        created_date = input("Введите дату создания (день-месяц-год): ").strip()
        deadline = input("Введите дедлайн (день-месяц-год): ").strip()

        notes.append({
            "Имя": user,
            "Заголовок": title,
            "Описание": description,
            "Статус": status,
            "Дата создания": created_date,
            "Дедлайн": deadline
        })

        another = input("Хотите добавить ещё одну заметку? (да/нет): ").strip().lower()
        if another != "да":
            break

    print("\nСписок заметок:")
    for i, note in enumerate(notes, 1):
        print(f"\n{i}. Имя: {note['Имя']}")
        print(f"   Заголовок: {note['Заголовок']}")
        print(f"   Описание: {note['Описание']}")
        print(f"   Статус: {note['Статус']}")
        print(f"   Дата создания: {note['Дата создания']}")
        print(f"   Дедлайн: {note['Дедлайн']}")

if __name__ == "__main__":
    multiple_notes()
