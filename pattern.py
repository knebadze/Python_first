row = int(input("please write number 1, 10"))
for i in range(0, row):
    for j in range(0, i +1):
        print("*", end=" ")
    print("\r")
for i in range (row, 0, -1):
    for j in range(0, i -1):
        print("*", end=" ")
    print("\r")

