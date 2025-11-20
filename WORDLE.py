import random
print("Ласкаво просимо в гру!")
print("У вас є 6 спроб щоб вгадати слово")
words = ["apple","house","water","green","happy","table","light","bread","fruit","sleep"]
words1 = random.choice(words)
attempts = 0
while True:
    if attempts > 6:
        break
    else:
        input_attempt = input("Спробуйте вгадати слово з 5 літер")
        if input_attempt != 5:
            print("Ви ввели слово, яке складається більше ніж з 5 літер")
        elif input_attempt == 5:
            attempts += 1
