import unittest
from emph import *

random.seed(1337)

text = "one two three four five"

class TestStringMethods(unittest.TestCase):

    def test_splitplaintext(self):
        self.assertEqual(splitplaintext(text), ["one", "two", "three", "four", "five"])

    def test_chooseemph(self):
        self.assertEqual(chooseemph(), ['<i>', '</i>'])
        self.assertEqual(chooseemph(), ['<em>', '</em>'])
        self.assertEqual(chooseemph(), ['<i>', '</i>'])
        self.assertEqual(chooseemph(), ['<i>', '</i>'])

    def test_applyemph(self):
        random.seed(1337)
        self.assertEqual(applyemph("one"), "<em>one</em>")


if __name__ == '__main__':
    unittest.main()
