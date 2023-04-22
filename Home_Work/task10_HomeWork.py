# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть. 
# Стороны монеты вводятся построчно или в одну строку, если умеете.
# Пример
# Ввод: 1 1 0 0 0 -> Вывод: 2
#Мой вариант
n = int(input("Сколько будет монет?: "))
arr = []
for d in range(n):
    arr.append(int(input("Введите  1-орел или 0-решка ")))

eagle= 0
tails = 0
for d in arr:
    if d ==0  or d< 0:
        tails += 1
    else:
        eagle +=1
if tails > eagle:
    print('переверните ',eagle, 'монетки орлом')
if tails==eagle:
    print('орлов и решек одинаково, без разницы как перевернуть')
else:
    print('переверните ', tails, 'монетки решка')


#Вариант преподавателя

num_coins = int(input("Сколько монет: "))
tails = 0
for i in range(num_coins):
    if input('Сторона монетки: ') == '0':
        tails += 1
if tails > num_coins - tails:
    print(num_coins - tails)
else:
    print(tails)

#Вариант со списком
coins = input().split()
heads = coins.count('1')
tails = coins.count('0')
print(f"минимальное колличество монет, \
которые нужно перевернуть: {min(heads, tails)}")

#Вариант со списком
coins = input().split(sep='')
heads = coins.count('1')
tails = coins.count('0')
print(f"минимальное колличество монет, \
которые нужно перевернуть: {min(heads, tails)}")