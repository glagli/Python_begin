# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в
# расчете на одного сотрудника.

gain = float(input('Введите выручку фирмы: '))
cost = float(input('Введите издержеки фирмы: '))

<<<<<<< HEAD
if gain >= cost:
    print('прибыль')
    print(f'Рентабельность: {((gain - cost) / gain):.2f}')
else:
    print('Фирма отработала с убытком')

number = int(input('Введите численность сотрудников фирмы: '))
if gain >= cost:
    print(f'прибыль фирмы в расчете на одного сотрудника: {((gain - cost) / number):.2f}')
else:
    print('Работала с убытком')
=======

print('прибыль' if gain >= cost else 'убыток')
print('Рентабельность: ', round((gain-cost)/gain, 3) if gain > cost else 'Фирма отработала с убытком')
number = int(input('Введите численность сотрудников фирмы: '))
print('прибыль фирмы в расчете на одного сотрудника: ', (gain-cost)/number if gain >= cost else 'Работала с убытком')
>>>>>>> lesson1