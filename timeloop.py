import sys
for i in sys.stdin:
    numberChant = int(i)
if 1<=numberChant<=100:
    a = 1
    while a <= numberChant:
        print(str(a) + " Abracadabra")
        a = a + 1
