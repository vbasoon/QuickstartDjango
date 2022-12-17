from unittest import TestCase

from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEqual(19, result)

    def test_minus(self):
        result = operations(23, 10, '-')
        self.assertEqual(13, result)

    def test_multiply(self):
        result = operations(23, 10, '*')
        self.assertEqual(230, result)
