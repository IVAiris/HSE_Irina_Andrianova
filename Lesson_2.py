# Lesson 2
# Ex.1


import json
import os

if os.path.exists("cases.json"):
    with open("cases.json", "r", encoding="utf-8") as f:
        cases = json.load(f)
else:
    cases = []

case_num = input("Укажи номер дела: ")

found_case = None
for case in cases:
    if case["Номер дела"] == case_num:
        found_case = case
        break

if found_case is not None:
    # дело найдено
    print(found_case)
else:
    # дела нет — спрашиваем участников и добавляем новое дело
    name_plaintiff = input("Укажи Истца: ")
    inn_plaintiff = int(input("Укажи ИНН Истца: "))
    name_defendant = input("Укажи Ответчика: ")
    inn_defendant = int(input("Укажи ИНН Ответчика: "))
    name_thirty_part = input("Укажи Третьего лица: ")
    inn_thirty_part = int(input("Укажи ИНН Третьего лица: "))

    plaintiff = {
        "Номер дела: ": case_num,
        "Название Истца: ": name_plaintiff,
        "Статус": "Истец",
        "ИНН Истца: ": inn_plaintiff,
    }

    defendant = {
        "Номер дела: ": case_num,
        "Название Ответчика: ": name_defendant,
        "Статус": "Ответчик",
        "ИНН Ответчика: ": inn_defendant,
    }

    thirty_part = {
        "Номер дела: ": case_num,
        "Название Третьего лица: ": name_thirty_part,
        "Статус": "Третье лицо",
        "ИНН Третьего лица: ": inn_thirty_part,
    }

    cases.append(
        {"Номер дела": case_num, "Участники спора": [plaintiff, defendant, thirty_part]}
    )
    print("Дело добавлено.")

with open("cases.json", "w", encoding="utf-8") as f:
    json.dump(cases, f, ensure_ascii=False, indent=2)


# cases = []
# case_num = input("Укажи номер дела")
# found_case = None
# for case in cases:
#     if case["Номер дела"] == case_num:
#         found_case = case
#         break

# if found_case is not None:
#     print(cases)

# else:
#     name_plaintiff = input("Укажи Истца: ")
#     inn_plaintiff = int(input("Укажи ИНН Истца: "))
#     name_defendant = input("Укажи Ответчика: ")
#     inn_defendant = int(input("Укажи ИНН Ответчика: "))
#     name_thirty_part = input("Укажи Третьего лица: ")
#     inn_thirty_part = int(input("Укажи ИНН Третьего лица: "))

#     plaintiff = {
#         "Номер дела: ": case_num,
#         "Название Истца: ": name_plaintiff,
#         "Статус": "Истец",
#         "ИНН Истца: ": inn_plaintiff,
#     }

#     defendant = {
#         "Номер дела: ": case_num,
#         "Название Ответчика: ": name_defendant,
#         "Статус": "Ответчик",
#         "ИНН Ответчика: ": inn_defendant,
#     }

#     thirty_part = {
#         "Номер дела: ": case_num,
#         "Название Третьего лица: ": name_thirty_part,
#         "Статус": "Третье лицо",
#         "ИНН Третьего лица: ": inn_thirty_part,
#     }

#     cases.append(
#         {"Номер дела": case_num, "Участники спора": [plaintiff, defendant, thirty_part]}
#     )

# print(cases)


# case_participants = [plaintiff, defendant, thirty_part]

# cases = [
#     {"Номер дела": case_num, "Участники спора": [plaintiff, defendant, thirty_part]}
# ]
