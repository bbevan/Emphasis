import unittest
from emph import *
import random

# pre-selected "random" numbers from the seed 123456789;
# they're in the array backwards for the sake of pop();
# the tests effictively synchronize r with the seed to
# the rng. This is its intended purpose.
text = "one two three four five"

em = ['<em>', '</em>']
b = ['<b>', '</b>']

class TestEmph(unittest.TestCase):
    r = [0,0,1,1,1,1,1,1,1,1] 
    s = 0

    def test_splitplaintext(self):
        self.assertEqual(splitplaintext(text), ["one", "two", "three", "four", "five"])

    def test_chooseemph(self):
        
        self.s = self.r.pop()

        if (s == 0): 
            self.assertEqual(chooseemph(123456789), em)
        elif (s == 1):
            self.assertEqual(chooseemph(123456789), b) 

    def test_applyemph(self):

        self.s = self.r.pop()

        if (s == 0): #applyemph chose not to apply the emphasis
            self.assertEqual(applyemph('one',123456789), 'one')
        elif (s==1):
            self.assertIn(applyemph('one',123456789), ['<b>one</b>' , '<em>one</em>'])
            
    
    # assert that r is in sync with the rng.
    # remember to run this as the last test.
    def test_r_sync(self):
        r = [0,0,1,1,1,1,1,1,1,1] 
        random.seed(123456789)
        for x in r:
            self.assertEqual(r.pop(), random.randint(0,1))



    #expected value function for chooseemph test
    def test_expectedvalue(self):
        i = 1000
        count = 0

        for x in range(i):
            if chooseemph() == em:
                count +=1

        self.assertAlmostEqual(count/i, 0.5, 1)
 

if __name__ == '__main__':
    unittest.main()
