"""
Із введеного користувачем речення 
потрібно вивести слова, що містять 
хоча б одну букву у верхньому регістрі.
"""
list = input("Введіть текст:")
count = len(list)
for i in range(0, count):
    if list[i].istitle():
        print(list[i])
