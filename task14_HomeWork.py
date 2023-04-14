# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.
# Пример
# Ввод: 17 -> Вывод: 1, 2, 4, 8, 16

right_side = int(input('rigth side: '))
degree = 0
num = []
while 2**degree<= right_side:
    num.append(2**degree)
    degree += 1
print(num)
print('______________________________________')

right_side = int(input('right side: '))
degree = 0
nums = []
while 2**degree <= right_side:
    nums.append(2**degree)
    degree += 1
print(nums)
print('______________________________________')

right_side = int(input('right side: '))
degree = 0
nums = {}
while 2**degree <= right_side:
    nums[degree] = 2**degree
    degree += 1
print(nums)
print('______________________________________')