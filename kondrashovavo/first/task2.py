"""
Вивести кількість пустих списків.
"""
a = [ 2, 4, [], 5, []]
sum = 0
count = len(a)
for i in range(0,count):
    if a[i] == []:
        sum = sum +1

print('Кількість порожніх списків', sum)

