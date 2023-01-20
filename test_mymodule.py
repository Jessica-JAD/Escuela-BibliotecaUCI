#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import doctest
import mymodule


class TestMyModule(unittest.TestCase):

    def test_get_prime_numbers(self):
        self.assertEqual(mymodule.get_prime_numbers(10), [2, 3, 5, 7])

    def test_is_prime(self):
        self.assertTrue(mymodule.is_prime(5))
        self.assertFalse(mymodule.is_prime(6))

    def test_sum(self):
        self.assertEqual(mymodule.sum(5, 7), 12)
        with self.assertRaises(TypeError):
            mymodule.sum(5, "Python")

    def test_get_prime_numbers(self):
        # Los números primos menores a 10 son necesariamente 2, 3, 5 y 7.
        self.assertEqual(mymodule.get_prime_numbers(10), [2, 3, 5, 7])

    def test_is_prime(self):
        # 5 es primo.
        self.assertTrue(mymodule.is_prime(5))
        # 6 no es primo.
        self.assertFalse(mymodule.is_prime(6))

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_default_widget_size(self):
        widget = widget('The widget')
        self.assertEqual(widget.size(), (50, 50))


    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

if __name__ == "__main__":
    unittest.main(verbosity=True)