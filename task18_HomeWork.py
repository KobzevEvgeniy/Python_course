# Задача 18: Требуется найти в массиве array_A[1..N] самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

N=abs(int(input("Введите количество элементов в массиве N ")))
Ai = input("Введите целые числа через пробел: ").split()
array_A= list(map(int, Ai))
if len(array_A) != N or N == 0:
    print('Введенное количество элементов, не соответствует заявленному количеству в массиве')
else:
    
    X = int(input('Введите число X: '))
    min=abs(X-array_A[0])
    position=0
    for i in range(1, N):
        count = abs(X - array_A[i])
        if count < min:
            min = count
            position = i
    print(f'Число {array_A[position]} самый близкий по величине к числу {X}')



#Вариант преподавателя
from random import randint
len_nums = int(input('Enter list length: '))
nums = [randint(1, 100) for i in range(len_nums)]
print("List: ", *nums)
x = int(input('Enter x: '))

# easy
min_diff = nums[0]
for i in nums:
    diff_current = abs(i-x)
    if diff_current < min_diff:
        res = i
        min_diff = diff_current

res = min([i for i in nums if abs(i-x) == min_diff])
print(f'Result is {res}')

# pro

print(f'Result is {min(nums, key=lambda y: abs(y-x))}')