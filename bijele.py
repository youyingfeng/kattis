import sys
input = sys.stdin.read()
inputList = input.split()

differenceKing = str(1 - int(inputList[0]))
differenceQueen = str(1 - int(inputList[1]))
differenceRook = str(2 - int(inputList[2]))
differenceBishop = str(2 - int(inputList[3]))
differenceKnight = str(2 - int(inputList[4]))
differencePawn = str(8 - int(inputList[5]))

print(differenceKing + ' ' + differenceQueen + ' ' + differenceRook + ' ' + differenceBishop + ' ' + differenceKnight + ' ' + differencePawn)
