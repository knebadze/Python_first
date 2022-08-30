# def multiply():
#     result = 10.5 * 4
#     return result

# answer = multiply()
# print(answer)

# def newFor(x, y):
#     result = x * y
#     return result

# for val in range(1, 5):
#     new = newFor(2, val)
#     print(new)


def fibonacci(n):
    if 0 <=n <= 1:
        return n
    
    n_minuse_1, n_minuse_2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minuse_2 + n_minuse_1
        n_minuse_2 = n_minuse_1
        n_minuse_1 = result
    return result

for i in range(36):
    print(i, fibonacci(i))
