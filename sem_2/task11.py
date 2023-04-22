# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

A = int(input("Введите число "))
fib0 = 0
fib1 = 1
fib2 = 1
i = 3
if A == 1:
    print("2 or 3")
elif A == 0:
    print("1")
else:
    while fib0 < A:
        fib0 = fib2 + fib1
        fib1 = fib2
        fib2 = fib0
        i += 1
    if A == fib0:
        print(i)
    else:
        print("-1")
