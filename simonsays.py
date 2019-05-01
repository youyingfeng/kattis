import sys
input = sys.stdin.readlines()
numberLines = int(input[0])

for lines in range(1, numberLines + 1):
    currentLine = input[lines]
    if currentLine[0:10] == 'Simon says':
        length = len(currentLine)
        print(currentLine[11:length]) #exclude space
