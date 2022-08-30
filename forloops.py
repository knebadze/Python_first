parrot = "Norwegian Blue"

for i in parrot:
    print(i)

number = '9, 230; 10. 20 4 6, 7;'
seperator = ""

for i in number:
    if not i.isnumeric():
        seperator = seperator + i

print(seperator)

#range
for i in range(1, 20):
    print(i)

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 12 == 0:
        break