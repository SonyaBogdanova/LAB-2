"5 ЗАДАЧА"
stroka=''
strokafinal=''
N = int(input("Введите кол-во слов: "))
a = 1

while a <= N:
    slovo = input("Введите слово: ")
    a += 1
    stroka = stroka + (slovo) + ', '

strokafinal=stroka[:-2]
print(strokafinal)
