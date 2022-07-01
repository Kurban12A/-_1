# Задание_1
num = int(input("Введите число: "))
while num != 0:
    if num > 0:
        print("Положительное")
    elif num < 0:
        print("Отрицательное")

    next_try = input("Продолжить:\nда/нет\n")
    if next_try == "да":
        num = int(input("Введите число еще раз: "))
    else:
        print("Ввод окончен")
        break

else:
    print("Ноль")
