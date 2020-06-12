# Hanoi algorithm (Recursive)
# We start with all n disks on the left peg and our goal is to place them in the right peg.

# Steps:
    #1. T(N-1 , left, right, middle) - Move top (N-1) disks from left to middle peg
    #2. T(1 , left, middle, right) - Move 1 disk from left to right peg
    #3. T(N-1 , middle, left, right) - Move top (N-1) disks from middle to right peg

def hanoi(height,left='left',right='right',middle='middle'):
    if(height):
        hanoi(height-1,left, middle, right)
        print(left,"->",right)
        hanoi(height-1, middle, right, left)

# Run the function
hanoi(5)
