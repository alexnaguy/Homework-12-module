import unittest
#Задание 2
#Создайте класс Калькулятор. В классе должна быть реализована следующая функциональность:
#■ Сложение двух чисел;
#■ Вычитание двух чисел;
#■ Умножение двух чисел;
#■ Деление двух чисел;
#■ Максимум из двух чисел;
#■ Минимум из двух чисел;
#■ Процент числа;
#■ Возведение числа в степень.
#Протестируйте все возможности созданного класса с помощью модульного тестирования (unittest).
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Деление на ноль невозможно")

    def maximum(self, a, b):
        return max(a, b)

    def minimum(self, a, b):
        return min(a, b)

    def percent(self, a, percent):
        return a * percent / 100

    def exponentiate(self, a, power):
        return a ** power


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 3), 4)

    def test_subtract(self):
        self.assertEqual(self.calculator.sub(10, 2), 8)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertRaises(ValueError, self.calculator.divide, 5, 0)

    def test_maximum(self):
        self.assertEqual(self.calculator.maximum(4, 9), 9)

    def test_minimum(self):
        self.assertEqual(self.calculator.minimum(3, 7), 3)

    def test_percentage(self):
        self.assertEqual(self.calculator.percent(40, 10), 4)

    def test_exponentiate(self):
        self.assertEqual(self.calculator.exponentiate(2, 4), 16)


if __name__ == '__main__':
    unittest.main()