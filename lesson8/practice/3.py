# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
# При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.
class OwnError(Exception):
    def __init__(self, text):
        self.text = text


myNumber = ''
lists = []
while "stop" not in myNumber:
    myNumber = input("Введите числа для формирования списка: ")
    try:
        for el in myNumber.split():
            if el.isdigit() == True:
                lists.append(el)
            elif el == "stop":
                break
            else:
                raise OwnError("Вы ввели не число")

    except OwnError as err:
        print(err)
        continue
    finally:
        print(*lists)
