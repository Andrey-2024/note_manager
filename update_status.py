#@title Статус обновления
def update_status():
    statuses = ["выполнено", "в процессе", "отложено"]
    current_status = "в процессе"  # Текущий статус заметки
    print(f"Текущий статус заметки: \"{current_status}\"")
    print("\nВыберите новый статус заметки:")
    for i, status in enumerate(statuses, 1):
        print(f"{i}. {status}")
    while True:
        try:
            choice = int(input("Ваш выбор: "))
            if 1 <= choice <= len(statuses):
                current_status = statuses[choice - 1]
                print(f"\nСтатус заметки успешно обновлён на: \"{current_status}\"")
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число.")

if __name__ == "__main__":
    update_status()
