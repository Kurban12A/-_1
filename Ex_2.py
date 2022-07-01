# Задание_2
num = int(input("Введите номер месяца: "))

dictionary = {1: 30, 2: "ФЕВРАЛЬ!", 3: 31,
              4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30,
              10: 31, 11: 30, 12: 30}

if num in dictionary and num != 2:
    print(f"Количество дней - {dictionary[num]}")
elif num == 2:
    print(f'ох уж этот {dictionary[num]}')
else:
    print("Число больше 12")