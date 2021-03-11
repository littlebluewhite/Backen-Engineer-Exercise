import unittest
from solution2 import increment, pipe


class PipeTestCase(unittest.TestCase):
    def setUp(self):
        self.args1 = (5, increment)
        self.args2 = (5, increment, increment, increment)

    def tearDown(self):
        self.args = None

    def test_function1(self):
        expected = 6
        result = pipe(*self.args1)
        self.assertEqual(expected, result)

    def test_function2(self):
        expected = 8
        result = pipe(*self.args2)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    solution2_tests = ['test_function1', 'test_function2']
    suite = unittest.TestSuite(map(PipeTestCase, solution2_tests))
