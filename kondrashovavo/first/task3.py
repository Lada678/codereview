"""
Вивести суми парних і непарних чисел списку.
"""
list = [2, 5, 7, 9, 8, 3, 4]
count = len(list)
sum1 = 0
sum2 = 0
for i in range(0, count):
    if  list[i] % 2 == 0:
        sum1 = sum1 + list[i]
    else:
        sum2 = sum2 + list[i]

print ("Сума парних  дорівнює", sum1)
print ("Сума непарних  дорівнює", sum2)
