# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, complex):
        self.c1 = complex

    def __add__(self, other):
        return f"Результат сложения множеств:{self.c1 + other.c1}"

    def __mul__(self, other):
        return f"Результат переумножения множеств: {self.c1 * other.c1}"


c1 = Complex(5+12j)
c2 = Complex(7-4j)
print(c1 + c2)
print(c1 * c2)
