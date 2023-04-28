# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Input:
# 1
# 2
# 5
# Output:
# 1, 3, 5, 7, 9

# Вариант №1
def arithmetic_progression(start, difference, amount):
    progression=[]
    for i in range(amount):
        progression.append(start)
        start=start+difference 
    return progression
    
s=int(input("Введите первый элемент прогрессии: "))
d=int(input("Введите разность элементов: "))
a=int(input("Введите количество элементов: "))
print(arithmetic_progression(s,d,a))

#Вариант №2 
print([(s+d*(a-1-i))  for i in range (a)]) 