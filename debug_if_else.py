answer = 5
print("please write number 1 to 10")

number = int(input())

# if number < answer:
#     print("please number higher")
#     number = int(input())
#     if number == answer:
#         print("well done")
#     else:
#         print("sorry, number not correctly")
# elif number > answer:
#     print("please number lower")
#     number = int(input())
#     if number == answer:
#         print("well done")
#     else:
#         print("sorry, number not correctly")
# else:
#     print("you got it first time")

# if number != answer:
#     if number < answer:
#         print("please higher number")
#     else:
#         print("please lower number")
#     number = int(input())
#     if number == answer:
#         print("well done")
#     else:
#         print("number is not correctly")
# else:
#     print("you are first")

if number == answer:
    print("you are first")
else:
    if number < answer:
        print("please higher number")
    else:
        print("please lower number")
    number = int(input())
    if number == answer:
        print("well done")
    else:
        print("number is not correctly")
