# GLORY BE TO GOD,
# RUNNING PYTHON CODE, 
# CREATING A PYTHON APPLICATION - PYTHON SEQUENCES,
# BY ISRAEL MAFABI EMMANUEL

import math

def fibonacci_number(nth_term:float)->int:
    gr:float = (1 + math.sqrt(5))/2
    fn:float = ((gr ** nth_term) - ((1 - gr) ** nth_term))/math.sqrt(5)
    if nth_term <= 0:
        return 0

    return round(fn)

def return_fibonacci(length:int)->list:
    numbers:list = []
    for i in range(0, length):
        numbers.append(fibonacci_number(i))
    
    return numbers

print(return_fibonacci(0))