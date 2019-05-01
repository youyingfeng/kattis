import sys
i = sys.stdin.read()
xy = i.split()
x = int(xy[0])
y = int(xy[1])
if -1000<=x<=1000 and -1000<=y<=1000 and x != 0 and y != 0:
    if x<0:
        if y<0:
            print('3')
        if y>0:
            print('2')

    if x>0:
        if y<0:
            print('4')
        if y>0:
            print('1')
