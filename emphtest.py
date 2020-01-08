import unittest
from emph import *
import random

# pre-selected "random" numbers from the seed 123456789;
# they're in the array backwards for the sake of pop();
# the tests effictively synchronize r with the seed to
# the rng. This is its intended purpose.
text = "one two three four five"
r = [0,0,1,1,1,1,1,1,1,1] 

class TestEmph(unittest.TestCase):

    def test_splitplaintext(self):
        self.assertEqual(splitplaintext(text), ["one", "two", "three", "four", "five"])

    def test_chooseemph(self):

        if (r.pop() == 0): 
            self.assertEqual(chooseemph(123456789), ['<em>', '</em>'])
        else:
            self.assertEqual(chooseemph(123456789), ['<b>', '</b>']) 

    def test_applyemph(self):

        if (r.pop() == 0): #applyemph chose not to apply the emphasis
            self.assertEqual(applyemph('one',123456789), 'one')
        else:
            result = applyemph('one',123456789)
            '<b>one</b>' or '<em>one</em>'
    
    # assert that r is in sync with the rng.
    # remember to run this as the last test.
    def test_r_sync(self):
        r = [0,0,1,1,1,1,1,1,1,1] 
        random.seed(123456789)
        for x in r:
            self.assertEqual(r.pop(), random.randint(0,1))


if __name__ == '__main__':
    unittest.main()
