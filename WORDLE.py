import colorama
from colorama import Fore, Back, Style

import random
print("Ласкаво просимо в гру!")
print("У вас є 6 спроб щоб вгадати слово")
words = ["apple","house","water","green","happy","table","light","bread","fruit","sleep"]
check = []
secret = random.choice(words)
attempts = 0
while attempts < 6:
    print(f"{attempts + 1} спроба із 6")
    input_attempt = input("Спробуйте вгадати слово з 5 літер")
    if input_attempt.isdigit():
        print("Треба вводити букви, а не цифри")
    else:
        if len(input_attempt) != 5:
            print("Ви ввели слово, яке складається більше або менше ніж з 5 літер")
            continue
        attempts = attempts + 1
        for index in range(5):
            if input_attempt[index] == secret[index]:
                check.append(f"{input_attempt[index]}-Green")
            elif input_attempt[index] in secret:
                check.append(f"{input_attempt[index]}-Yellow")
            else:
                check.append(f"{input_attempt[index]}-NoMach")
        check.append("---")
        print(check)
        if input_attempt == secret:
            print("Вітаю, ви вгадали")
            print(f"Кількість використаних спроб: {attempts}")
            break
else:
    print(f"Нажаль спроби закінчилися, ви програли :(. Правильне слово було: {secret}")
