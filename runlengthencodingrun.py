import sys
input = sys.stdin.read()
inputSplit = input.split()

operation = inputSplit[0]

if operation == 'E':
    string = inputSplit[1]
    length = len(string)

    encoded = ''
    number = 1
    if length == 1:
        encoded = string[0] + '1'

    else:
        for letter in range(1, length):
            if string[letter] == string[letter-1]:
                number += 1
            else:
                encoded = encoded + string[letter-1] + str(number)
                number = 1
            if letter == (length - 1):
                encoded = encoded + string[letter] + str(number)

    print(encoded)

if operation == 'D':
    string = inputSplit[1]
    length = len(string)

    decoded = ''
    for letter in range(0, length, 2):
        number = int(string[letter + 1])
        decoded = decoded + (number * string[letter])

    print(decoded)
