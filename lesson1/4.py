# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
number = int(input("Ведите число: "))
my_max = 0
while number != 0:
    a = number % 10
    if a > my_max:
        my_max = a
    number = number // 10
print('Cамая большая цифра в числе ', my_max)