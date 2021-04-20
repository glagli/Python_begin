#  Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его
# завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
# завершаем цикл. Во втором также необходимо предусмотреть условие, при котором
# повторение элементов списка будет прекращено
import itertools

myList = []
myCycleList = []
number = int(input("Введите число с которого начнётся последовательность: "))
endNumber = int(input("Введите число на котором последовательность закончится: "))
for i in itertools.count(number):
    if i > endNumber:
        break
    else:
        myList.append(str(i))
myList.append(' ')
myList = ' '.join(myList)
print('Сгенерируемые целые числа, начиная с указанного', myList)
c = 0
for j in itertools.cycle(myList):
    if c == len(myList) * 4:
        break
    myCycleList.append(j)
    c += 1
print('Четырёхкратное повторение элементов cгенерируемой последовательности: ', ''.join(myCycleList))