
#loop
for i in range( 1,13 ):
    print("No. {0} squared is {1} and cubed is {2}" .format(i, i ** 2, i ** 3))

a = 45
b = 15
c = 3

print(a - b / c)

quantity = 10
price = 5.0
total = quantity * price
tax = total / 5

Total = total + tax

print(total)
days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])