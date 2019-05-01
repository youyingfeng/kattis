import sys
input = str(sys.stdin.read())
length = len(input)

name = input[0]

for letter in range(1, length):
    if input[letter] == input[letter - 1]:
        continue
    else:
        name = name + input[letter]

print(name)
