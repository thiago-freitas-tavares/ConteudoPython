# Hello World + Regras Básicas

print('Hello, World')
print("Hello, World")

i = '''
Hello, World.
Thank you,Thiago.
'''
print(i)

age = 35
price = 19.95
first_name = "Thiago"
is_online = False
print(first_name, "is", age, "years old")
print(first_name + " is " + str(age) + " years old")
print(f'{first_name} is [{age}] years old')     # f de format string

name = input("What is your name? ")
print("Hello", name)

birth_year = input("Enter your birth year: ")
age = 2023 - int(birth_year)
print("Your age is", age)

# Converter Variável

int()
float()
bool()
str()
