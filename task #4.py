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
