"""
@Author: Wiktor Filipiuk <wiktor.filipiuk@gmail.com>
@ProblemName: Large sum
-----------------------------------------------------------------------
@Description:
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
.
.
.
(All numbers can be found in file "50_digits_numbers.txt")
"""

import numpy as np

f = open("50_digits_numbers.txt", "r")
input = f.read()

numbers = input.split("\n")
collected_digits = []
step = 0

for i in range(len(numbers[0])):
    tmp = np.sum([int(x[-(i+1)]) for x in numbers])
    digits = str(tmp)
    
    if len(collected_digits) < (len(digits) + step):
            for k in range((len(digits) + step) - len(collected_digits)):
                collected_digits.insert(0, [])
    
    for j in range(len(digits)):
        collected_digits[-(j+1+step)].append(int(digits[-(j+1)]))
    
    step = step + 1
  
summed_digits = [sum(element) for element in collected_digits]

for i in range(len(summed_digits)):
    current_summed = str(summed_digits[-(i+1)])
    current_summed_length = len(current_summed)
    if current_summed_length > 1:
        for j in range(1, len(current_summed)):
            to_move, to_stay = divmod(summed_digits[-(i+1)], 10)
            summed_digits[-(i+1)] = to_stay
            summed_digits[-(i+1+1)] = summed_digits[-(i+1+1)] + to_move
            
print(summed_digits)
answer = ''.join([str(value) for value in summed_digits[:10]])
print("First 10 digits of the solution of this problem are: {0}".format(answer))



