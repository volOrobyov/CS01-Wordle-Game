from colorama import Style, Fore
import random

print("---ЛАСКАВО ПРОСИМО У ГРУ WORDLE---!")
print("У вас є 6 спроб щоб вгадати слово")
words = ["apple","house","water","green","happy","table","light","bread","fruit","sleep"]
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
        check = ["ВВЕДЕНЕ СЛОВО:"]
        for index in range(5):
            if input_attempt[index] == secret[index]:
                check.append(Fore.GREEN + input_attempt[index] + Style.RESET_ALL)
                comment = (Fore.LIGHTGREEN_EX + f"{input_attempt[index]} Стоїть на своєму місті" + Style.RESET_ALL)
            elif input_attempt[index] in secret:
                check.append(Fore.YELLOW + input_attempt[index] + Style.RESET_ALL)
                comment = (Fore.LIGHTYELLOW_EX + f"{input_attempt[index]} Є в слові, але не стоїть на своєму місті" + Style.RESET_ALL)
            else:
                check.append(Fore.RED + input_attempt[index] + Style.RESET_ALL)
                comment = (Fore.LIGHTRED_EX + f"{input_attempt[index]} Цієї літери немає в слові" + Style.RESET_ALL)
            print(comment)
        print("------------------------------------------------")
        print(' '.join(check))
        if input_attempt == secret:
            print("Вітаю, ви вгадали")
            print(f"Кількість використаних спроб: {attempts}")
            break
            #Вже зробив, тому просто додам нотаток
else:
    print(f"Нажаль спроби закінчилися, ви програли :(. Правильне слово було: {secret}")
