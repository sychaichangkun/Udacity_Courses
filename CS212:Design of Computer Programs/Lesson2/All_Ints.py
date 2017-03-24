# ------------
# User Instructions
#
# Define a function, all_ints(), that generates the 
# integers in the order 0, +1, -1, +2, -2, ...

def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    # Your code here.
    yield 0
    num=0
    while True:
        num+=1
        yield +num
        yield -num

