"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Longest Collatz Sequence
-----------------------------------------------------------------------
@Description:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import numpy as np
import time

def getCollatzSequence(start):
    currentValue = start
    sequence = []
    sequence.append(start)
    while currentValue > 1:
        if currentValue%2 == 0:
            currentValue = currentValue // 2
            sequence.append(currentValue)
        else:
            currentValue = 3*currentValue + 1
            sequence.append(currentValue)
    return(sequence)
    
    

def findLongestSequence(min, max):
#-- Brute-force approach
    currentLength = 0
    result = None
    candidates = list(range(min, max+1))
    for candidate in candidates:
        candidateLength = len(getCollatzSequence(candidate))
        if candidateLength > currentLength:
            currentLength = candidateLength
            result = candidate
    return(result)

start_time = time.time()
answer = findLongestSequence(13, 1000000)
print("Longest Colatz Sequence obtains for: ".format(answer))
end_time = time.time() - start_time
print("Operation lasted: {0} sec.".format(end_time))


