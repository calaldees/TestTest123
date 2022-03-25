import unittest
from app.example import Die

class TestDie(unittest.TestCase):

    def setUp(self):
        self.die = Die()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


    def test_ChangeSides(self):

        self.die.ChangeSides(7)

        self.assertEqual(self.die.GetSides(),7)
