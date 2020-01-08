import random
import fileinput

emphasis = [['<em>', '</em>'], ['<i>', '</i>']]


def splitplaintext(text):
    return text.split()

def chooseemph():
    coin2 = random.randint(0,1)
    return emphasis[coin2]

def applyemph(myString):
    coin1 = random.randint(0,1)
    emph = chooseemph()

    if (coin1 == 1):
        return emph[0] + myString + emph[1]
    else:
        return myString

def splititerate(text):
    emphtext = []
    mytext = splitplaintext(text)
    for word in mytext:
        emphtext.append(applyemph(word))

    return emphtext

# the whitespace separator for joining individuals words back together
s = " "

def emphasize():
    print("<html><body>")
    for line in fileinput.input():
        emphtext = splititerate(line)
        print(s.join(emphtext))
    print("</body></html>")
