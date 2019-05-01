import sys
input = sys.stdin.read()
xy = input.split()
x = xy[0]
y = xy[1]

invx = x[::-1]
invy = y[::-1]

if int(invx) > int(invy):
    print(invx)
if int(invy) > int(invx):
    print(invy)
