import unittest
from line import Line
from utils import are_parallel, are_perpendicular


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def test_parallel(self):
        r1 = Line()
        r2 = Line()
        r1.explicit_form(1, 20)
        r2.from_two_points([2, 2], [4, 4])
        self.assertTrue(are_parallel(r1=r1, r2=r2))

    def test_perpendicular(self):
        r1 = Line()
        r2 = Line()
        r1.explicit_form(-1, 20)
        r2.from_two_points([2, 2], [4, 4])
        self.assertTrue(are_perpendicular(r1=r1, r2=r2))


if __name__ == '__main__':
    unittest.main()
