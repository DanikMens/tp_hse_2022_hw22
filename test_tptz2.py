from unittest import TestCase, main
import time

from tptz2 import _min
from tptz2 import _max
from tptz2 import _sum
from tptz2 import mult
class tptz2test(TestCase):
    def test_minimum(self):
        time_start = time.time()
        self.assertEqual(_min([1, 2, 3, 4, 5]), 1)
        print('Потраченное время на функцию  _min = ', time.time() - time_start)
    def test_maximum(self):
        time_start = time.time()
        self.assertEqual(_max([1, 3, 5, 7, 9]), 9)
        print('Потраченное время на функцию  _max = ', time.time() - time_start)
    def test_summa(self):
        time_start = time.time()
        self.assertEqual(_sum([1, 3, 4, 2, 1]), 11)
        print('Потраченное время на функцию  _sum = ', time.time() - time_start)
    def test_umnozhenie(self):
        time_start = time.time()
        self.assertEqual(mult([1, 3, 4, 2, 5]), 120)
        print('Потраченное время на функцию  _mult = ', time.time() - time_start)
    def test_moi(self):
        self.assertIsNot(_min, None)

if __name__ == '__main__':
    main()




