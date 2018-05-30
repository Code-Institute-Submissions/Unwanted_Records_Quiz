import unittest
import run
import operator


class TestRun(unittest.TestCase):
    
    def test_int(self):
        """ Tests to make sure that scores will be passed as integers """
        a = 2
        b = int(2)
        self.assertEqual(a, b)
    
    def test_sort(self):
        """ Tests that the sort function is working """
        scores = [5,9,6,14,11]
        sort = sorted(int(scores), reverse=True)
        self.assertEqual(sort, [14,11,9,6,5])


if __name__ == '__main__':
    unittest.main()