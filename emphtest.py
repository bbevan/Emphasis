import unittest
from emph import *

text = "one two three four five"

class TestStringMethods(unittest.TestCase):

    def test_splitplaintext(self):
        self.assertEqual(splitplaintext(text), ["one", "two", "three", "four", "five"])

    def test_chooseemph(self):
        random.seed(1337)
        if (random.randint(0,1) == 0):
            self.assertEqual(chooseemph(), ['<em>', '</em>'])
        else:
            self.assertEqual(chooseemph(), ['<b>', '</b>'])
        #self.assertEqual(chooseemph(), ['<b>', '</b>'])
        #self.assertEqual(chooseemph(), ['<em>', '</em>'])
        #self.assertEqual(chooseemph(), ['<b>', '</b>'])
        #self.assertEqual(chooseemph(), ['<em>', '</em>'])

    def test_applyemph(self):
        random.seed(1337)
        #self.assertEqual(applyemph("one"), "<b>one</b>")
        self.assertEqual(applyemph("two"), "<em>two</em>")


if __name__ == '__main__':
    unittest.main()
