# 1
# Поработайте с переменными, создайте несколько, выведите на экран. Запросите у
# пользователя некоторые числа и строки и сохраните в переменные, а затем
# выведите на экран. Используйте функции для консольного ввода input() и
# консольного вывода print().
# Попробуйте также через встроенную функцию id() понаблюдать, какие типы
# объектов могут изменяться и сохранять за собой адрес в оперативной памяти.

# name = input("Введи свое имя")
# age = int(input("Введи своЙ возраст"))
# learn_py_str = input("Ты учишь Питон: да или нет?")
# learn_py = learn_py_str.lower() in ("да", "y", "yes")
# print(name, age, learn_py)


# answer = input("Да/нет/yes/y: ")
# result = answer.lower() in ("да", "y", "yes")
# print(result)

# name = input("Введи свое имя: ")
# print("Привет,", name)


# name = input("Введи свое имя")
# age = int(input("Введи своЙ возраст"))
# learn_py_str = input("Ты учишь Питон: да или нет?")
# learn_py = (
#     "Молодец!" if learn_py_str.lower() in ("да", "y", "yes") else ("Много теряешь)")
# )
# print(name, age, learn_py)

# Работа с переменной

name = input("Введи свое имя")
age = int(input("Введи своЙ возраст"))
learn_py_str = input("Ты учишь Питон: да или нет?")

print("DEBUG:", repr(learn_py_str.lower()))

learn_py = (
    "Молодец!"
    if learn_py_str.strip().lower() in ("да", "y", "yes")
    else "Много теряешь)"
)
print(name, age, learn_py)

# x = 6
# if x > 0:
#     print(x, id(x))
#     x = x + 1
#     print(x, id(x))
# print("Inaught")

# x = 6
# print(x, id(x))
# if x > 0:
#     x = x + 1
#     print(x, id(x))
# print("Inaught")

# работа с генератором

for x in range(0, 7):
    if x > 3:
        print(x, id(x))
    else:
        print("got_it")


# работа со списком

my_list = [1, 2, 3, 4, 5]
print(id(my_list))
my_list.append(99)
print(my_list, id(my_list))

# Ex.2
# Пользователь вводит время в секундах. Рассчитайте время и сохраните отдельно
# в каждую переменную количество часов, минут и секунд. Переведите время в
# часы, минуты, секунды и сохраните в отдельных переменных.
# Используйте приведение типов для перевода строк в числовые типы.
# Предусмотрите проверку строки на наличие только числовых данных через
# встроенный строковый метод .isdigit().
# Выведите рассчитанные часы, минуты и секунды по отдельности в консоль.

time_sec = input("Сколько секунд? ")
if time_sec.isdigit():
    time_sec = int(time_sec)
    time_hours = time_sec // 3600
    time_min = (time_sec % 3600) // 60
    time_sec_end = (time_sec % 3600) % 60
    print(f"Часов: {time_hours}, минут {time_min} и секунд {time_sec_end}")
else:
    print("Введи количество секунд! Целое!")


# Ex.3
#  Запросите у пользователя через консоль число n (от 1 до 9). Найдите сумму чисел
# n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
# Выведите данные в консоль.

# n = input()
# nn = n * 2
# nnn = n * 3
# n = int(n)
# if 1 <= n <= 9:
#     print(n + int(nn) + int(nnn))
# else:
#     print("Введи от 1 до 9: ")


n = input()
if n.isdigit():
    nn = n * 2
    nnn = n * 3
    n = int(n)
    if 1 <= n <= 9:
        print(n + int(nn) + int(nnn))
    else:
        print("Введи от 1 до 9: ")
else:
    print("Введи число, от 1 до 9, пж, и запусти снова")
