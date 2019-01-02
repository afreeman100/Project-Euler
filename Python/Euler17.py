def getUnits(n):
    unitDict = {
        0 : "",
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
    }
    return unitDict.get(n)


def getTens(n):
    teenDict = {
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteen",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen"
    }
    tenDict = {
        20 : "twenty",
        30 : "thirty",
        40 : "forty",
        50 : "fifty",
        60 : "sixty",
        70 : "seventy",
        80 : "eighty",
        90 : "ninety",
    }
    if n<10:
        return getUnits(n)
    if n<20:
        return teenDict.get(n)
    else:
        return tenDict.get(n//10*10)+getUnits(n%10);


def getHundreds(n):
    if n%100==0:
        return getUnits(n//100)+"hundred"

    return getUnits(n//100)+"hundredand"+getTens(n%100)


def buildWord(n):
    if n<10:
        return getUnits(n)

    if n<100:
        return getTens(n)

    if n<1000:
        return getHundreds(n)

    return getUnits(n//1000)+ "thousand"



words = []
for x in range(1,1000+1):
    words.append(buildWord(x))

totalLength = 0
for word in words:
    totalLength += len(word)


print(words)
print(totalLength)
