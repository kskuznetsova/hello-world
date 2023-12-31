
# modified code taken from here: https://realpython.com/python-rock-paper-scissors/

import random

user_action = input("Choose your fighter: ")
# выбор игрока записывается в переменную

print("Щас компьютер вам ответит...")

possible_actions = ["камень", "ножницы", "бумага"]
computer_action = random.choice(possible_actions)

print(f"\nВы выбрали {user_action}, компьютер выбрал {computer_action}.\n")
# это и есть f-строка в питоне

# определяем победителя
if user_action == computer_action:
    print(f"Оба игрока выбрали {user_action}. Ничья!")
elif user_action == "камень":
    if computer_action == "ножницы":
        print("Вы выиграли!")
    else:
        print("Вы проиграли.")
elif user_action == "бумага":
    if computer_action == "камень":
        print("Вы выиграли!")
    else:
        print("Вы проиграли.")
elif user_action == "ножницы":
    if computer_action == "бумага":
        print("Вы выиграли!")
    else:
        print("Вы проиграли.")
else:
    print("Ну и что вы ввели?")
