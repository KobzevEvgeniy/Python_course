# 39. Даны два массива чисел. Требуется вывести те уникальные элементы первого массива
#  (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. 
# Элементы обоих массивов вводятся в две строки через пробел.
# Пример:
# 1 2 3 4 5 6
# 4 5 6 7 8 -> 1 2 3


list_1 = input('Введите элементы первого массива через пробел: ').split()
list_2 = input('Введите элементы второго массива через пробел: ').split()

print(*[int(elem) for elem in list_1 if elem not in list_2])