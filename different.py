import sys
for line in sys.stdin:
    input = line.split()
    a = int(input[0])
    b = int(input[1])
    print(abs(a - b))
