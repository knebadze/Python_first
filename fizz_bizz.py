from ast import Num
from unittest import result


def fizz_bizz(number: int) -> int:
    if number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "bizz"
    elif number % 15 == 0:
        return "fizz_bizz"
    else:
        return str(number)
    
for i in range(1, 100):
    print(fizz_bizz(i))


# factorial

def factorial(n: int) -> int:
    """
    return
    """
    if n <= 1:
        return 1
    # result = 2
    # for x in range(3, n + 1):
    #     result *= x
    # return result

    return n * factorial(n - 1)
for i in range(36):
    print(factorial(i))

# number of argumnets

def sum_numbers(*arg: float) -> float:
    """
    return
    """
    # variant 1
    result = 0
    for number in arg:
        result += number

    return result

    # variant 2
    # return sum(arg)
    
print(sum_numbers(1, 2, 3))

