# parrot= "Norwegian Blue"
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])
# print()
# text = "W\ne\n\nW\ni\nn"
# print(text)
# print()
# print(text[5])
from ast import Num


def sum_eo(n, t):

    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))

string = input("e or o: ")
number = int(input("number: "))
x = sum_eo(number, string)
print(x)
