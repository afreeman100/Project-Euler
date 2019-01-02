#read and split
f = open("names22.txt", 'r')
names = f.read().replace('"', "").split(',')
names.sort()

print(names)

totalSum = 0
for i, name in enumerate(names):
    nameValue = 0
    for letter in name:
        val = ord(letter)-64
        nameValue += val
    nameValue *= (i+1)
    totalSum += nameValue

print(totalSum)
