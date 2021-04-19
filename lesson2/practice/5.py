# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если
# в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же
# значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]

number = float(input('Введите число: '))
myList = [8, 7, 5, 3, 3]

if number in myList:
    myList.insert(myList.index(number)+myList.count(number), number)
else:
    for elm in myList:
        if number > elm:
            myList.insert(myList.index(elm), number)
            break
        elif number < min(myList):
            myList.append(number)
print(myList)

# Способ через sort и reverse
# myList.append(number)
# myList.sort(reverse=True)
# print(myList)
