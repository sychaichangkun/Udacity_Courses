"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""
from itertools import permutations

def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    ## your code here; you are free to define additional functions if needed
    weekdays = (1,2,3,4,5)
    res = [
            (Hamming,Knuth,Minsky,Simon,Wilkes)            
            for Hamming, Knuth, Minsky, Simon, Wilkes in permutations(weekdays, 5)
            if Knuth == Simon + 1
            for laptop, droid, tablet, iphone in permutations(weekdays, 4)
            if laptop == 3
            if tablet is not 5
            if iphone is 2 or tablet is 2
            for programmer, writer, manager, designer in permutations(weekdays, 4)
            if programmer is not Wilkes
            if (programmer is Hamming and droid is Wilkes) or (programmer is Wilkes and droid is Hamming)
            if writer is not Minsky
            if Knuth == manager + 1 and tablet is not manager
            if designer is not 4 and designer is not droid
            if (laptop is 1 and Wilkes is writer) or (Wilkes is 1 and laptop is writer)
            ]

    result = (('Hamming',res[0][0]), ('Knuth',res[0][1]), ('Minsky',res[0][2]),('Simon',res[0][3]), ('Wilkes',res[0][4]))   
    return  [x[0] for x in  sorted(result, key = lambda x:x[1])]
logic_puzzle()