# Hanoi algorithm
# Steps:
    #1. T(N-1 , Beg, End, Aux) - Move top (N-1) disks from Beg to Aux peg
    #2. T(1 , Beg, Aux, End) - Move 1 disk from Beg to End peg
    #3. T(N-1 , Aux, Beg, End) - Move top (N-1) disks from Aux to End peg

def hanoi(height,left='left',right='right',middle='middle'):
    if(height):
        hanoi(height-1,left, middle, right)
        print(left,"->",right)
        hanoi(height-1, middle, right, left)

hanoi(5)