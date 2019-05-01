import sys
input = sys.stdin.read()
inputSplit = input.split()
numberArticles = int(inputSplit[0])
impactFactor = int(inputSplit[1])

minimumScientists = numberArticles * (impactFactor - 1) + 1
print(minimumScientists)
