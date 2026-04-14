# Lesson 3
# 1. Создайте ряд функций для проведения математических вычислений:

# ● функция вычисления факториала числа (произведение натуральных чисел от 1 до
# n). Принимает в качестве аргумента число, возвращает его факториал;

n = int(input())


def factorial(n):
    g = 1
    for i in range(1, n + 1):
        g = g * i
    return g


print(f"Факториал числа {n} равен {factorial(n)}")


# ● поиск наибольшего числа из трёх. Принимает в качестве аргумента кортеж из трёх
# чисел, возвращает наибольшее из них;


def max_chislo(num):
    a, b, c = num
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m


a = int(input("Будем сравнивать три числа. Введи первое: "))
b = int(input("Введи второе: "))
c = int(input("И последнее: "))

num = (a, b, c)

print(f"Максимальное из трех чисел {max_chislo (num)}")


# ● расчёт площади прямоугольного треугольника. Принимает в качестве аргумента
# размер двух катетов треугольника. Возвращает площадь треугольника.

cat1 = float(input("Введи катет 1 в сантиметрах, до 2 знаком после ТОЧКИ: "))
cat2 = float(input("Введи катет 2 в сантиметрах, до 2 знаком после ТОЧКИ: "))


def S_triangle(cat1, cat2):
    s = (cat1 * cat2) / 2
    return s


print(
    f"""
       Площадь прямоугольного треугольника с катетами {cat1:.2f} и {cat2:.2f}:
       {S_triangle(cat1, cat2):.2f} сантиметров квадратных"""
)


# 2. Создайте функцию для генерации текста с адресом суда.
# Функция должна по шаблону генерировать шапку для процессуальных документов с
# реквизитами сторон для отправки.
# Пример работы функции:
# В арбитражный суд города Москвы
# Адрес: 115225, г. Москва, ул. Б. Тульская, 17
# Истец: Пупкин Василий Геннадьевич
# ИНН 1236182357 ОГРНИП 218431927812733
# Адрес: 123534, г. Москва, ул. Водников, 13
# Ответчик: ООО “Кооператив Озеро”
# ИНН 1231231231 ОГРН 123124129312941
# Адрес: 123534, г. Москва, ул. Красивых молдавских партизан, 69
# Номер дела А40-123456/2023
# Функция должна принимать в качестве аргумента словарь с данными ответчика и
# номером дела (ссылка на файл с данными).
# ● На основании номера дела из списка судов должен быть выбран корректный суд
# для отправки. Данные по арбитражным судам есть в указанном выше файле.
# Используйте код суда из дела.
# ● С помощью f-string создайте шаблон для заполнения.
# ● В качестве истца укажите свои данные.
# ● В данные по ответчику подставьте данные, переданные в функцию в качестве
# аргумента.
# ● В конце шапки подставьте номер дела.
# Функция должна возвращать готовую шапку в виде строки.
# Создайте ещё одну функцию, которая принимает в себя список словарей с данными
# ответчика. Используйте цикл for для генерации всех возможных вариантов этой шапки с
# вызовом первой функции внутри тела цикла for и выводом данных, которые она
# возвращает в консоль.

# with open("lesson_2_data.py", "r", encoding="utf-8") as f:

#     i = 0
#     for line in f:
#         print(line)
#         i += 1
#         if i > 10:
#             break


# respondents: dict {**kwargs}

# with open("lesson_2_data.py", "r", encoding="utf-8") as f:
#     lines = f.readlines()

# for line in lines[3:854]:
#     print(line)


# courts = {}


# respondents = {}

# with open("lesson_2_data.py", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     line.strip().split()
#     respondents ('full_name') = value

# Версия кода - не работает: ошибочное допущение о формате файла:
# что в строке все нужные поля строго лежат в виде пар ключ:
# значение, разделённых запятыми.
# При этом встречаются одиночные элементы, а не пары (из-за того, что функция удаляет "," и ":" не только между элементами словаря, но и внутри них).

# respondents = {}

# with open("lesson_2_data.py", "r", encoding="utf-8") as f:
#     i = 0
#     for line in f:
#         line = line.strip()
#         parts = line.split(",")
#         respondent = {}
#         for part in parts:
#             key, value = part.split(":")

#             if key == "full_name":
#                 respondent["full_name"] = value
#             if key == "inn":
#                 respondent["inn"] = value
#             if key == "ogrn":
#                 respondent["ogrn"] = value
#             if key == "address":
#                 respondent["address"] = value
#             if key == "case_number":
#                 respondent["case_number"] = value

#         respondents[i] = respondent
#         i += 1
# print(respondents[0])
# print(respondents[1])
# print(respondents[2])


import ast


def get_court_by_code(court_code, filepath="lesson_2_data.py"):
    lines = []
    inside = False

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("courts = ["):
                inside = True
            if inside:
                lines.append(line)
                if line.strip().endswith("]"):
                    break

    raw = "".join(lines)
    raw = raw[raw.index("[") : raw.rindex("]") + 1]
    courts_list = ast.literal_eval(raw)

    courts = {c["court_code"]: c for c in courts_list}

    return courts.get(court_code)  # None если код не найден


# проверка участка кода, где извлекаются данные суда:

# court = get_court_by_code("А40")
# print(court["court_name"])  # Арбитражного суда города Москвы
# print(court["court_address"])  # 115225 Москва, ул. Большая Тульская, 17
# print(get_court_by_code("А99"))  # None — несуществующий код


def generate_header(respondent):
    case_number = respondent["case_number"]
    court_code = case_number.split("-")[0]
    court = get_court_by_code(court_code)

    return f"""В {court['court_name'].replace ('Арбитражного суда', 'Арбитражный суд')}
Адрес: {court['court_address']}
____________________________________________
Истец: А Ирина Владимировна
паспорт 00 00 № 000000
Адрес: г. Москва, Московская ул., д 1
____________________________________________
Ответчик: {respondent['short_name']}
ИНН {respondent['inn']} ОГРН {respondent['ogrn']}
Адрес: {respondent['address']}
____________________________________________
Номер дела {case_number}"""


# # Проверка участка кода с генерацией шапки - на данных одного из  ответчиков
# test = {
#     "short_name": 'ООО "ПРОДСЕРВИС"',
#     "inn": "2465081302",
#     "ogrn": "1042402640125",
#     "address": "660020, Красноярский край, г. Красноярск...",
#     "case_number": "А33-2794/2011",
# }
# print(generate_header(test))

# Функция для генерации всех шапок:


def generate_all_headers(respondents_list):
    for respondent in respondents_list:
        if "case_number" in respondent:
            print(generate_header(respondent))
            print()  # пустая строка между шапками


# Функция парсит словари ответчиков:


def get_respondents_by_code(filepath="lesson_2_data.py"):
    lines = []
    inside = False

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("respondents = ["):
                inside = True
            if inside:
                lines.append(line)
                if line.strip().endswith("]"):
                    break

    raw = "".join(lines)
    raw = raw[raw.index("[") : raw.rindex("]") + 1]
    courts_list = ast.literal_eval(raw)
    return courts_list


# Счетчик для проверки работы кода:
respondents = get_respondents_by_code()

count = 0
for respondent in respondents:
    if "case_number" in respondent:
        print(generate_header(respondent))
        print("_" * 44)
        count += 1
    if count == 5:
        break
