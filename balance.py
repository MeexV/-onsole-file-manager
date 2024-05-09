import os


def save_balance(balance):
    with open("balance.txt", "w") as f:
        f.write(str(balance))


def load_balance():
    if os.path.exists("balance.txt"):
        with open("balance.txt", "r") as f:
            return int(f.read())
    else:
        return 0


def save_history(history):
    with open("history.txt", "w") as f:
        for item in history:
            f.write(f"{item[0]}: {item[1]}\n")


def load_history():
    history = []
    if os.path.exists("history.txt"):
        with open("history.txt", "r") as f:
            for line in f:
                name, cost = line.strip().split(": ")
                history.append((name, int(cost)))
    return history


def balance():
    balance = load_balance()
    history = load_history()

    while True:
        print()
        print(f"Ваш счет: {balance}")
        print('1. пополнение счета ')
        print('2. покупка ')
        print('3. история покупок ')
        print('4. выход ')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            try:
                cost = abs(int(input("Введите сумму пополнения: ")))
                balance += cost
            except ValueError:
                print("Введите числовое значение!")
            except:
                print("Введите корректное значение!")
        elif choice == '2':
            try:
                cost = abs(int(input("Введите сумму покупки: ")))
                if cost > balance:
                    print("Недостаточно средств на счете!")
                else:
                    balance -= cost
                    name = input("Введите название покупки: ")
                    history.append((name, cost))
            except ValueError:
                print("Введите числовое значение!")
        elif choice == '3':
            print("История покупок:")
            [print(f"{item[0]}: {item[1]}") for item in history]
        elif choice == '4':
            save_balance(balance)
            save_history(history)
            break
        else:
            print('Неверный пункт меню')
