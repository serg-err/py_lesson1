'''Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
a = 1
while a < 6:
    print(a, '0')
    a = a + 1

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
c = 0
a = 1
while a < 11:
    b = input('введите цифру')
    if b == '5':
        c = c + 1
    a = a + 1
print('Количество введенных цифр 5:', c)

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

a = 0
for i in range(101):
    a += i
print(a)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

a = 1
for i in range(1, 11):
    a *= i
print(a)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
a = 123456

while a > 0:
    print(a % 10)
    a = a // 10

# -------------------------------------------
'''
Задача 5 
Вывести цифры числа на каждой строчке ПОПОРЯДКУ.
'''
a = 123456789
b = a
i = 0
while b > 0:
    b % 10
    b = b // 10
    i = i + 1
# Узнали количество цифр
b = a
i = i - 1
while i != -1:
    b = a
    k = 0
    while k < i:
        q = b % 10
        b = b // 10
        k = k + 1
    print(b % 10)
    i = i - 1

# -----------------------------------------------

'''
Задача 6
Найти сумму цифр числа.
'''

a = 1234
sum = 0
while a > 0:
    b = a % 10
    sum = sum + b
    a = a // 10
print('сумма цифр числа = ', sum)

'''
Задача 7
Найти произведение цифр числа.
'''

a = 123456789
sum = 1
while a > 0:
    b = a % 10
    sum = sum * b
    a = a // 10
print('произведение цифр числа = ', sum)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''

a = 123456
five = 'no'
while a > 0:
    b = a % 10
    if b == 5:
        five = 'yes'
    a = a // 10
print(five)

'''
Задача 9
Найти максимальную цифру в числе
'''

a = 123456789
c = 0
while a > 0:
    b = a % 10
    if b > c:
        c = b
    a = a // 10
print('максимальная цифра в числе - ', c)

'''
Задача 10
Найти количество цифр 5 в числе
'''

a = 1234567895
c = 0
kolvo = 0
while a > 0:
    b = a % 10
    if b == 5:
        c = b
        kolvo = kolvo + 1
    a = a // 10
print('количество цифр 5 в числе - ', kolvo)

