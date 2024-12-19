class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result_coeffs = [0] * max_len

        for i in range(len(self.coefficients)):
            result_coeffs[i] += self.coefficients[i]

        for i in range(len(other.coefficients)):
            result_coeffs[i] += other.coefficients[i]

        return Polynomial(result_coeffs)

    def evaluate(self, x):
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * (x ** i)
        return result

    def derivative(self):
        deriv_coeffs = [i * coeff for i, coeff in enumerate(self.coefficients)][1:]
        return Polynomial(deriv_coeffs)

    def to_file(self, filename):
        with open(filename, 'w') as file:
            for i, coeff in enumerate(self.coefficients):
                if coeff != 0:
                    file.write(f"{coeff} * x^{i} + ")
            file.write("0\n")

    def find_integer_roots(self):
        if all(isinstance(coeff, int) for coeff in self.coefficients):
            integer_roots = []
            for i in range(-100, 101):
                if self.evaluate(i) == 0:
                    integer_roots.append(i)
            return integer_roots
        else:
            return []

    def __str__(self):
        terms = []
        for i, coeff in enumerate(self.coefficients):
            if coeff != 0:
                terms.append(f"{coeff} * x^{i}")
        return " + ".join(terms) + " = 0"


p1 = Polynomial([1, 2, 1])
p2 = Polynomial([1, 3, 2])

p3 = p1 + p2
print("Сумма многочленов:", p3)

value = p1.evaluate(2)
print("Значение в точке 2:", value)

deriv = p1.derivative()
print("Производная:", deriv)

p1.to_file('polynomial.txt')

roots = p1.find_integer_roots()
print("Целые корни:", roots)
