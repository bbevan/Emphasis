import unittest
from emph import *

# pre-selected "random" numbers from the seed 123456789;
# they're in the array backwards for the sake of pop();
# the tests effictively synchronize r with the seed to
# the rng. This is its intended purpose.
r = [0,0,1,1,1,1,1,1,1,1]
text = "one two three four five"

class TestEmph(unittest.TestCase):

    def test_splitplaintext(self):
        self.assertEqual(splitplaintext(text), ["one", "two", "three", "four", "five"])

    def test_chooseemph(self):
        s = r.pop()

        if (s == 0):
            result = chooseemph(123456789)
            self.assertEqual(chooseemph(123456789), result)
        else:
            result = chooseemph(123456789)
            self.assertEqual(chooseemph(123456789), result) 

    def test_applyemph(self):
        q = r.pop()
        #self.assertEqual(applyemph('one', seed), '<em>one</em>')
        #self.assertEqual(applyemph('one', seed), '<b>one</b>')

        if (q == 0):
            result = applyemph('one',123456789)
            self.assertEqual(applyemph('one',123456789), result)
        else:
            result = applyemph('one', 123456789)
            self.assertEqual(applyemph('one',123456789), result)


if __name__ == '__main__':
    unittest.main()
