import unittest
import solution1


class NumericFormatTestCase(unittest.TestCase):
    def setUp(self):
        self.args1 = (9527,)
        self.args2 = (3345678,)
        self.args3 = (-1234.45,)

    def tearDown(self):
        self.args = None

    def test_function1(self):
        expected = "9,527"
        result = solution1.numeric_format(*self.args1)
        self.assertEqual(expected, result)

    def test_function2(self):
        expected = "3,345,678"
        result = solution1.numeric_format(*self.args2)
        self.assertEqual(expected, result)

    def test_function3(self):
        expected = "-1,234.45"
        result = solution1.numeric_format(*self.args3)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    solution1_tests = ['test_function1', 'test_function2', 'test_function3']
    suite = unittest.TestSuite(map(NumericFormatTestCase, solution1_tests))
