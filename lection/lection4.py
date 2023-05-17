#Дан список чисел. необходимо выбрать из списка только четные и потом вывести чилсо и его кврадрат

# вариант 1
size=int(input("№1 введите макс число до которого будет ряд: "))
list_6=[i for i in range (size) if i%2==0]
print(list_6)
print(f"{[i*i for i in range (size) if i%2==0]}")

# вариант 2
data=list(map(int, input("№2 Введите список чисел через пробел: ").split()))
res=list()
def mach(data)->res:
    for i in data:
        if i%2==0:
            res.append((i, i**2))
    return res

print(mach(data))
# вариант 3
data=list(map(int, input("№3 Введите список чисел через пробел: ").split()))
res=list()
for i in data:
    if i%2==0:
        res.append((i, i**2))
print(res)

# вариант 4
def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]
data=list(map(int, input("№4 Введите список чисел через пробел: ").split()))
res2=select(int, data)
print(res2)
res2= where(lambda x: x %2==0, res2)
print(res2)
res2=list(select(lambda x: (x, x**2),res2))
print(res2)

#функция фильтр
data=list(map(int, input("Введите список чисел через пробел: ").split()))
res3= list(filter(lambda x: x %10==5, data))
print(res3)

# вариант 5
data=[1, 2, 3, 5, 8, 15, 23, 38]
res= map(int, data)
res=filter(lambda x: x %2==0, res)
res=list(map(lambda x: (x, x**2), res))
print(f" Вариант №5 ответ: {res}")



