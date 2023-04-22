# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

N=int(input("Введите количество элементов в массиве N "))
Ai = input("Введите целые числа через пробел: ").split()
array_A= list(map(int, Ai))
if len(array_A) != N or N == 0:
    print('Введенное количество элементов, не соответствует заявленному количеству в массиве')
else:
    x=int(input("Введите число X  "))
    count = [array_A[i] for i in range( len(array_A)) if array_A[i] ==x]
    print(f"{array_A} --> {len(count)}")


# Вариант преподавателя
len_nums = int(input('Enter list length: '))
nums = [randint(1, 100) for i in range(len_nums)]
print("List: ", *nums)
x = int(input('Enter x: '))

# easy
print(f'{x} finds in list {nums.count(x)} times')

# hard
print(f'{x} finds in list {len([i for i in nums if i == x])} times')