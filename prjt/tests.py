import unittest
from pyramid import testing


def cube(n):
    return n ** 3

def square(n):
    return n ** 2



class TutorialViewTests(unittest.TestCase):

    def test_cube(self):
        self.assertEqual( cube(5),125)
        self.assertEqual( cube(10),1000)
        self.assertEqual( cube(0),0)
    def test_area(self):
        self.assertEqual( square(2), 4)
        self.assertEqual( square(6), 36)
        self.assertEqual( square(20), 400)
