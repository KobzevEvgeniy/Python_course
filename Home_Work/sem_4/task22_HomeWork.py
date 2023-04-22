# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#  Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит в строку первый список затем на следующией строке второй список.

#вариант 1
from random import randint
first_set = set(randint(1, 20) for result_list in range(int(input('Введите кол-во элементов первого множества: '))))
print(first_set)
second_set = set(randint(1, 20) for result_list in range(int(input('Введите кол-во элементов второго множества: '))))
print(second_set)
sorted_set = sorted(first_set.intersection(second_set))
print(*sorted_set)

#вариант 2
leng_first=int(input("Введите количество элементов первого набора чисел: "))
number_1=input("Введите целые числа через пробел: ").split()
first_list={int(number_1[i]) for i in range(leng_first)}
print(first_list)

leng_second=int(input("Введите количество элементов второго набора чисел: "))
number_2=input("Введите целые числа через пробел: ").split()
second_list={int(number_2[i]) for i in range(leng_second)}
print(second_list)

result_list=first_list.intersection(second_list)                
print(sorted(result_list))