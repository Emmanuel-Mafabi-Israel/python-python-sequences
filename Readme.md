# Python Sequence Types, Israel Mafabi Emmanuel

Python Sequence Types. 🤭😍

`.py` file located in lib folder...

To run the tests, use `pytest`

## Fibonacci Sequence Example

In this example, we'll use Python to create functions that generate Fibonacci numbers. Fibonacci numbers are a sequence where each number is the sum of the two preceding ones, usually starting with 0 and 1.

### Fibonacci Function

Below is the Python code that defines two functions:
1. `fibonacci_number`: Calculates the nth Fibonacci number.
2. `return_fibonacci`: Generates a list of Fibonacci numbers up to a specified length.

```python
import math

def fibonacci_number(nth_term: float) -> int:
    gr: float = (1 + math.sqrt(5)) / 2
    fn: float = ((gr ** nth_term) - ((1 - gr) ** nth_term)) / math.sqrt(5)
    if nth_term <= 0:
        return 0
    return round(fn)

def return_fibonacci(length: int) -> list:
    numbers: list = []
    for i in range(0, length):
        numbers.append(fibonacci_number(i))
    return numbers

print(return_fibonacci(0))
```

### Explanation

- `fibonacci_number(nth_term: float) -> int`:
  - This function calculates the Fibonacci number for a given term using Binet's formula.
  - `gr` is the golden ratio.
  - It returns the rounded Fibonacci number for the given `nth_term`.
- `return_fibonacci(length: int) -> list`:
  - This function generates a list of Fibonacci numbers up to the specified `length`.
  - It iterates from 0 to `length` and appends each Fibonacci number to the `numbers` list.

## Usage

To use these functions, simply call `return_fibonacci` with the desired length of the Fibonacci sequence:

python

```
print(return_fibonacci(10))
```

This will print the first 10 Fibonacci numbers.

## Conclusion

This example demonstrates how to work with sequence types in Python by generating Fibonacci numbers. 

~ Glory be to God!!!

Happy coding! 🤭😉😍