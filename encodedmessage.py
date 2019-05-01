import sys
import math
input = sys.stdin.readlines()
numberCases = int(input[0])

for lines in range(1, numberCases + 1):
    encodedMessage = input[lines]
    squareLength = int(math.sqrt(len(encodedMessage)))

    decodedString = ''

    for a in range(squareLength -1, -1 , -1):
        currentLine = encodedMessage[a::squareLength]
        decodedString = decodedString + currentLine

    print(decodedString)
