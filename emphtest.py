import unittest
from emph import *

# pre-selected "random" numbers from the seed 123456789;
# they're in the array backwards for the sake of pop();
# the tests effictively synchronize r with the seed to
# the rng. This is its intended purpose.
text = "one two three four five"

class TestEmph(unittest.TestCase):

    def test_splitplaintext(self):
        self.assertEqual(splitplaintext(text), ["one", "two", "three", "four", "five"])

    def test_chooseemph(self):
        r = [0,0,1,1,1,1,1,1,1,1,0]
        s = r.pop()

        if (s == 0): 
            self.assertEqual(chooseemph(123456789), ['<em>', '</em>'])
        else:
            self.assertEqual(chooseemph(123456789), ['<b>', '</b>']) 

    def test_applyemph(self):
        r = [0,0,1,1,1,1,1,1,1,0]
        s = r.pop()

        if (s == 0): #applyemph chose not to apply the emphasis
            self.assertEqual(applyemph('one',123456789), 'one')
        else:
            result = '<b>one</b>'
            '<b>one</b>' or '<em>one</em>'


if __name__ == '__main__':
    unittest.main()
