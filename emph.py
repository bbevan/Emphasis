import random
import fileinput

emphasis = [['<em>', '</em>'], ['<b>', '</b>']]


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

def main():
    a = '''
    <!doctype html>

    <html lang="en">
    <head>
    <meta charset="utf-8">

    <title>Emphasize.py</title>
    <meta name="description" content="The HTML5 Herald">
    <meta name="author" content="SitePoint">

    <link rel="stylesheet" href="css/styles.css?v=1.0">

    </head>

    <body>
    '''
    
    print(a)
    
    for line in fileinput.input():
        emphtext = splititerate(line)
        print(s.join(emphtext))
    
    print("</body></html>")

if __name__ == 'main':
    main()