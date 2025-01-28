#@title Крайний Срок проверки
from datetime import datetime

def check_deadline():
    today = datetime.now()
    print(f"Текущая дата: {today.strftime('%d-%m-%Y')}")
    while True:
        deadline_input = input("Введите дату дедлайна (в формате день-месяц-год): ").strip()
        try:
            deadline = datetime.strptime(deadline_input, "%d-%m-%Y")
            if deadline < today:
                delta = (today - deadline).days
                print(f"Внимание! Дедлайн истёк {delta} дней назад.")
            else:
                delta = (deadline - today).days
                print(f"До дедлайна осталось {delta} дней.")
            break
        except ValueError:
            print("Некорректный формат даты. Попробуйте снова.")

if __name__ == "__main__":
    check_deadline()
