word1 = input("Введите пароль: ")
word2 = input("Введите пароль ещё раз: ")

if word1 == word2:
    print ("Пароль принят")
else:
    print ("Пароль не принят")


"2 ЗАДАЧА"

"Cхемы расположения мест в плацкартных"
"Плацкартный вагон (54 места) Номера нижних мест — нечётные, а верхних — чётные. Места с 37 по 54 — боковые. "


chislo = int(input("Введите номер места: "))

if (chislo<1) or (chislo >54):
    print("В плацкарте только 54 места!")

if (chislo >0) and (chislo<55):
    if (chislo % 2) == 0:
        s1='чётное'
    else:
        s1='Нечётное'
    if (chislo>36) and (chislo<55):
        s2='боковое'
    else:
        s2='купе'

print("Ваше место — ", s1,", ", s2)

"3 ЗАДАЧА"
year_number=int(input("Введите год: "))

if ((year_number % 4 == 0) and (year_number % 100 != 0)) or (year_number % 400 ==0):
    print("Год ", year_number, " — Високосный")
else:
    print("Год ", year_number, " — Не високосный")

"4 ЗАДАЧА"
color1 = input("Введите 1-ый цвет: ")
color2 = input("Введите 2-ой цвет: ")

if color2=='красный' and color1=='синий':
    print("Результат: фиолетовый")
if color1=='красный' and color2=='синий':
    print("Результат: фиолетовый")

if color1=='красный' and ((color2=='жёлтый') or (color2=='желтый')):
    print("Результат: оранжевый")
if color2=='красный' and ((color1=='жёлтый') or (color1=='желтый')):
    print("Результат: оранжевый")

if color1=='синий' and ((color2=='жёлтый') or (color2=='желтый')):
    print("Результат: зелёный")
if color2=='синий' and ((color1=='жёлтый') or (color1=='желтый')):
    print("Результат: зелёный")

