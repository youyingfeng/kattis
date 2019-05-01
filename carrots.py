import sys
i = sys.stdin.read()
xy = i.split()
x = int(xy[0])
y = int(xy[1])
if 1<=x and y<=1000:
    print(y)
