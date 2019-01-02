f = open("Euler59Cipher.txt", 'r')
read = f.read().split(',')

encrypted = [int(char) for char in read]


def decryptWith(decryptKey):
    keyRep = [decryptKey[0], decryptKey[1], decryptKey[2]]

    # pad key length
    while len(keyRep) < len(encrypted):
        keyRep.extend(keyRep)

    # decrypt each character and join to make string
    decrypt = [chr(char ^ keyRep[c]) for c, char in enumerate(encrypted)]
    decrypt = "".join(decrypt)

    return decrypt


def getDecryptions():
    possible = []
    #all possible decryption combinations
    for i in range(ord('a'), ord('z') + 1):
        for j in range(ord('a'), ord('z') + 1):
            for k in range(ord('a'), ord('z') + 1):

                key = [i, j, k]
                val = decryptWith(key)
                possible.append((key, val))

    return possible


def bestDecryption():
    decryptions = getDecryptions()

    best = None
    maxSpace = 0

    #return decryption which has the most space characters
    for d in decryptions:
        spaceCount = 0
        for char in list(d[1]):
            if char == ' ':
                spaceCount += 1
        if spaceCount > maxSpace:
            maxSpace = spaceCount
            best = d

    #decryptionKey = best[0]
    decryptionPhrase = best[1]

    return decryptionPhrase


def asciiSum(string):

    count = 0
    chars = list(string)

    for char in chars:
        count += ord(char)

    return count


phrase = bestDecryption()
print(phrase)
print(asciiSum(phrase))
