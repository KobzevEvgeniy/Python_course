# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
#  Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять 
# из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются 
# друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам  


def find_letter(words) -> int:
    """
    Проверяет слова на ритм. Подсчитывает количество гласных букв
    """
    return sum(1 for i in words if i in 'аеёиоуыэюя')
    
    
phrase = str(input("Введите фразу: "))
string = phrase.lower().split()
temp = find_letter(string[0])
if all([find_letter(i) == temp for i in string]):
    print('Парам пам-пам')
else:
    print('Пам парам')