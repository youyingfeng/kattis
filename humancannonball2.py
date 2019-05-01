import sys
import math

input = sys.stdin.readlines()
length = int(input[0])

for lines in range(1, length + 1):
    currentLine = input[lines]
    numbers = currentLine.split()
    v0 = float(numbers[0])
    angle = math.radians(float(numbers[1]))
    x1 = float(numbers[2])
    h1 = float(numbers[3])
    h2 = float(numbers[4])

    t = x1 / (v0 * math.cos(angle))
    y = (v0 * t * math.sin(angle)) - (0.5 * 9.81 * (t ** 2))

    if (y - h1) > 1 and (h2 - y) > 1:
        print('Safe')
    else:
        print('Not Safe')
