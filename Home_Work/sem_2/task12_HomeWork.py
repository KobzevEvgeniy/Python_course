# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# Пример:
# Ввод: 5 6 -> Вывод: 2 3
#Мой вариант
sum_result = int(input("Введите сумму загаданных натуральных чисел X и Y (X,Y≤1000): "))
mult_result = int(input("Введите произведение загаданных натуральных чисел X и Y (X,Y≤1000): "))
x = 0

while (x < 1001):
    if x * x - sum_result * x + mult_result == 0:
        break
    x += 1
if x == 1001 or mult_result == 0:
    print("Введены некорректные данные.")
else:
    print(f"Ввод: {sum_result}, {mult_result} -> Вывод: {x}, {sum_result - x}")
print("__________________")

#вариант 2
s_sum = int(input('sum: '))
p_mult = int(input('mult: '))
flag = True
for x in range(s_sum):
    if x * (s_sum - x) == p_mult:
        print(f'result: {x} {s_sum - x}')
        flag = False
        break
if flag:
    print('No results: ')
print("__________________")

#вариант преподавателя для любых чисел
S = int(input('Введите сумму:  '))
P = int(input('Введите произведение:  '))

x = (S + (S**2 - 4*P)**(0.5)) / 2
y = (S - (S**2 - 4*P)**(0.5)) / 2
print(x, y)