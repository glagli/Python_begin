#  Реализовать программу работы с органическими клетками, состоящими из ячеек.
#  Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
# до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
# равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n*****.
from random import randint


class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f"{self.cell}"

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell - other.cell > 0:
            return Cell(self.cell - other.cell)
        else:
            return 'разность количества ячеек двух клеток меньще нуля'

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __floordiv__(self, other):
        return Cell(round(self.cell // other.cell))

    def make_order(self, row):
        result = ''
        for i in range(self.cell // row):
            result += f"{'+' * row}\n"
        result += f"{'+' * (self.cell % row)}"
        return result


cell_1 = Cell(randint(1, 25))
cell_2 = Cell(randint(1, 25))
print(f'Ячеек в первой клетке: {cell_1}\nЯчеек во второй клетке: {cell_2}\n')
print(
    f'Объединение двух клеток: {cell_1 + cell_2}\nВычитание клеток: {cell_1 - cell_2}\nУмножение клеток:'
    f' {cell_1 * cell_2}\nЦелочисленное деление клеток: {cell_1 // cell_2}\n'
)

num = randint(1, 7)
print(f'реализация метода make_order с параметром row = {num}:\n{cell_1.make_order(num)}')
