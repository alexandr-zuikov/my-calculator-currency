first_name = input("Ваше имя:")
last_name = input("Ваше фамилия:")

print("Добрый день, " + last_name+ " " + first_name)

print("Спасибо за внимание, " + first_name + "!")

RUB=input("Введите сумму в рублях:")
US=input("Введите курс US по ЦБ РФ:")
GEL=input("Введите курс GEL по ЦБ Грузии:")

print("Вот ваш калькулятор валют:")

def kurs():
    sum1 = float(RUB)/float(US)
    print("В долларах =", sum1)
    sum2 = sum1 * float(GEL)
    print("В лари =", sum2) 
    return "Спасибо за использование калькулятора!"

print(kurs())