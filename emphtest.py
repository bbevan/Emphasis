import unittest
from emph import *

text = "one two three four five"

class TestStringMethods(unittest.TestCase):

    def test_splitplaintext(self):
        self.assertEqual(splitplaintext(text), ["one", "two", "three", "four", "five"])

    def test_chooseemph(self):
        random.seed(1337)
        self.assertEqual(chooseemph(), ['<i>', '</i>'])
        self.assertEqual(chooseemph(), ['<b>', '</b>'])
        self.assertEqual(chooseemph(), ['<i>', '</i>'])
        self.assertEqual(chooseemph(), ['<i>', '</i>'])

    def test_applyemph(self):
        random.seed(1337)
        self.assertEqual(applyemph("one"), "<b>one</b>")
        self.assertEqual(applyemph("two"), "<i>two</i>")


if __name__ == '__main__':
    unittest.main()
