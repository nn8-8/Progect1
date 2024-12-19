import copy
import math

class Matrix:
    def __init__(self, file_path=None, data=None):
        if file_path:
            self.load_from_file(file_path)
        elif data is not None:
            self.data = data
        else:
            self.data = []

    def load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.data = [list(map(float, line.split())) for line in file]
        except Exception as e:
            print(f"Ошибка при загрузке файла")
            self.data = []

    def save_to_file(self, file_path):
        try:
            with open(file_path, 'w') as file:
                for row in self.data:
                    file.write(' '.join(map(str, row)) + '\n')
        except Exception as e:
            print(f"Ошибка при сохранении файла")

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            print("Матрицы должны иметь одинаковые размеры для сложения")
            return None
        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(data=result)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = []
            for row in self.data:
                result.append([element * other for element in row])
            return Matrix(data=result)
        elif isinstance(other, Matrix):
            if len(self.data[0]) != len(other.data):
                print("Несовместимые размеры для умножения")
                return None
            result = []
            for i in range(len(self.data)):
                row = []
                for j in range(len(other.data[0])):
                    sum_ = 0
                    for k in range(len(other.data)):
                        sum_ += self.data[i][k] * other.data[k][j]
                    row.append(sum_)
                result.append(row)
            return Matrix(data=result)
        else:
            return None

    def transpose(self):
        result = []
        for j in range(len(self.data[0])):
            row = []
            for i in range(len(self.data)):
                row.append(self.data[i][j])
            result.append(row)
        return Matrix(data=result)

    def determinant(self):
        if len(self.data) != len(self.data[0]):
            print("Определитель определен только для квадратных матриц")
            return None
        return self._determinant(self.data)

    def _determinant(self, matrix):
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        elif n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            det = 0
            for c in range(n):
                minor = self._get_minor(matrix, 0, c)
                det += ((-1) ** c) * matrix[0][c] * self._determinant(minor)
            return det

    def _get_minor(self, matrix, row, col):
        minor = copy.deepcopy(matrix)
        del minor[row]
        for i in range(len(minor)):
            del minor[i][col]
        return minor

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

def create_sample_matrices():
    matrix1_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2_data = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

    with open('matrix1.txt', 'w') as file:
        for row in matrix1_data:
            file.write(' '.join(map(str, row)) + '\n')
    with open('matrix2.txt', 'w') as file:
        for row in matrix2_data:
            file.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    create_sample_matrices()

    matrix1 = Matrix(file_path='matrix1.txt')
    matrix2 = Matrix(file_path='matrix2.txt')

    matrix_sum = matrix1 + matrix2
    if matrix_sum:
        print("Сумма матриц:")
        print(matrix_sum)

    matrix_scaled = matrix1 * 3
    if matrix_scaled:
        print("Матрица, умноженная на 3:")
        print(matrix_scaled)

    matrix_product = matrix1 * matrix2
    if matrix_product:
        print("Произведение матриц:")
        print(matrix_product)

    matrix_transposed = matrix1.transpose()
    print("Транспонированная матрица:")
    print(matrix_transposed)

    determinant = matrix1.determinant()
    if determinant is not None:
        print("Определитель матрицы:")
        print(determinant)

    if matrix_sum:
        matrix_sum.save_to_file('matrix_sum.txt')
