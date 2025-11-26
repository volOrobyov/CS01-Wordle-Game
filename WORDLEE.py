from colorama import Style, Fore
import random

print("Ласкаво просимо в гру!")
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
        check = []
        for index in range(5):
            if input_attempt[index] == secret[index]:
                check.append(Fore.GREEN + input_attempt[index] + Style.RESET_ALL)
            elif input_attempt[index] in secret:
                check.append(Fore.YELLOW + input_attempt[index] + Style.RESET_ALL)
            else:
                check.append(Fore.RED + input_attempt[index] + Style.RESET_ALL)
        print(' '.join(check))
        if input_attempt == secret:
            print("Вітаю, ви вгадали")
            print(f"Кількість використаних спроб: {attempts}")
            break
            #Вже зробив в попередніх комітах, тому просто додам нотаток (перемога\поразка)
else:
    print(f"Нажаль спроби закінчилися, ви програли :(. Правильне слово було: {secret}")