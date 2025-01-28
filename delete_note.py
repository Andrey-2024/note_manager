#@title Удалить Заметку
def delete_note():
    notes = [
        {"Имя": "Алексей", "Заголовок": "Список покупок", "Описание": "Купить продукты на неделю"},
        {"Имя": "Мария", "Заголовок": "Учеба", "Описание": "Подготовиться к экзамену"}
    ]

    print("\nТекущие заметки:")
    for i, note in enumerate(notes, 1):
        print(f"\n{i}. Имя: {note['Имя']}")
        print(f"   Заголовок: {note['Заголовок']}")
        print(f"   Описание: {note['Описание']}")

    target = input("\nВведите имя пользователя или заголовок для удаления заметки: ").strip()

    updated_notes = [note for note in notes if note["Имя"] != target and note["Заголовок"] != target]

    if len(updated_notes) < len(notes):
        print("\nУспешно удалено. Остались следующие заметки:")
        for i, note in enumerate(updated_notes, 1):
            print(f"\n{i}. Имя: {note['Имя']}")
            print(f"   Заголовок: {note['Заголовок']}")
            print(f"   Описание: {note['Описание']}")
    else:
        print("\nЗаметка не найдена.")

if __name__ == "__main__":
    delete_note()
