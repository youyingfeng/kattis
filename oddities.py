import sys
i = sys.stdin.read()
listNumbers = i.split()
numberCases = int(listNumbers[0])

for a in range(numberCases):
    testCase = int(listNumbers[a + 1])
    if testCase % 2 == True:
        print(str(testCase) + " is odd")
    else:
        print(str(testCase) + " is even")
