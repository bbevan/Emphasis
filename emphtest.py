import unittest
from emph import *

text = "one two three four five"

class TestEmphasis(unittest.TestCase):

    def randtest(self, method1, output1, output2, seed):
        random.seed(seed)
        r = random.randint(0,1)
        if (r == 0):
            self.assertEqual(method1, output1)
        else:
            self.assertEqual(method2, output2)
    
    def test_splitplaintext(self):
        self.assertEqual(splitplaintext(text), ["one", "two", "three", "four", "five"])

    def test_chooseemph(self):
        random.seed(12345)
        r = random.randint(0,1)
        if (r == 1):
            self.assertEqual(chooseemph(12345), ['<b>', '</b>'])
        else:
            self.assertEqual(chooseemph(), ['<em>', '</em>'])

    def test_applyemph(self):
        r = random.randint(0,1)
        if (r == 1):
            self.assertEqual(applyemph("one", 12345), "<b>one</b>")
        else:
            self.assertEqual(applyemph("one", 12345), "<em>one</em>")


if __name__ == '__main__':
    unittest.main()
