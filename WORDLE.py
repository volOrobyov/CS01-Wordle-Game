import random
print("Ласкаво просимо в гру!")
print("У вас є 6 спроб щоб вгадати слово")
words = ["apple","house","water","green","happy","table","light","bread","fruit","sleep"]
secret = random.choice(words)
attempts = 0
while attempts < 6:
    print(f"{attempts + 1} спроба із 6")
    input_attempt = input("Спробуйте вгадати слово з 5 літер")
    if len(input_attempt) != 5:
        print("Ви ввели слово, яке складається більше або менше ніж з 5 літер")
        continue
    attempts = attempts + 1
    for i in range(5):
        if input_attempt[i] == secret[i]:
            print(f"{input_attempt[i]} - Green")
        elif input_attempt[i] in secret:
            print(f"{input_attempt[i]} - yellow")
        else:
            print(f"{input_attempt[i]} - NoMatch")
    if input_attempt == secret:
        print("Вітаю, ви вгадали")
        break
else:
    print("Нажаль спроби закінчилися, ви програли")