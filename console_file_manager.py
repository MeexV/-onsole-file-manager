import os
import sys
import shutil

import balance
import victory

def name_creator(name):
    return name


if __name__ == "__main__":
    while True:
        print()
        print('1. создать папку ')
        print('2. удалить (файл/папку) ')
        print('3. копировать (файл/папку) ')
        print('4. просмотр содержимого рабочей директории ')
        print('5. посмотреть только папки ')
        print('6. посмотреть только файлы ')
        print('7. просмотр информации об операционной системе ')
        print('8. создатель программы ')
        print('9. играть в викторину ')
        print('10. мой банковский счет ')
        print('11. выход ')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            os.mkdir(input("Введите имя папки: "))
        elif choice == '2':
            ans = input("Что вы хотите удалить?: ")
            if ans == "файл":
                os.remove(input("Введите имя файла: "))
            else:
                os.rmdir(input("Введите имя папки: "))
        elif choice == '3':
            ans = input("Что вы хотите удалить?: ")
            if ans == "файл":
                shutil.copy(input("Введите имя файла, который хотите скопировать: "), input("Введите новое имя файла: "))
            else:
                shutil.copytree(input("Введите имя папки, который хотите скопировать: "), input("Введите новое имя папки: "))
        elif choice == '4':
            print(os.listdir())
            ans = input("Сохранить содержимое рабочей директории в файл? (да/нет): ")
            if ans == "да":
                files = []
                dirs = []
                [dirs.append(entry) if os.path.isdir(entry) else files.append(entry) for entry in os.listdir()]
                with open("listdir.txt", "w") as f:
                    f.write(f"files: {', '.join(files)} \ndirs: {', '.join(dirs)}")
        elif choice == '5':
            [print(entry) for entry in os.listdir() if os.path.isdir(entry)]
        elif choice == '6':
            [print(entry) for entry in os.listdir() if os.path.isfile(entry)]
        elif choice == '7':
            print(sys.platform)
        elif choice == '8':
            print(name_creator("Voronin Maxim"))
        elif choice == '9':
            victory.game()
        elif choice == '10':
            balance.balance()
        elif choice == '11':
            break
        else:
            print('Неверный пункт меню')
