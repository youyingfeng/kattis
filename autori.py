import sys
input = sys.stdin.read()
stringLength = len(input)

outputString = input[0]

for i in range(1, stringLength - 1):
    if input[i] == '-':
        outputString = outputString + input[i + 1]

print(outputString)
