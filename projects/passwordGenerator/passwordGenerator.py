import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
numberForLetters= int(input("How many letters would you like in your password? "))
numberForSymbols = int(input("How many symbols would you like? "))
numberForNumbers = int(input("How many numbers would you like? "))

passwordList = []

for char in range(1, numberForLetters + 1):
    passwordList.append(random.choice(letters))

for char in range(1, numberForSymbols + 1):
    passwordList.append(random.choice(symbols)) 

for char in range(1, numberForNumbers + 1):
    passwordList.append(random.choice(numbers)) 

random.shuffle(passwordList)
password = ""
for char in passwordList:
    password = password + char
print(f"Your password is: {password}")

