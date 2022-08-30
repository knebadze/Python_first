# print("please choose")
#
# print("1:\tLearn Python")
# print("2:\tLearn java")
# print("3:\tGo Swimming")
# print("0:\tExit")
choice = "-"
while choice != "0":
    if choice in "123":
        print("Your Chose {}".format(choice))
    else:
        print("please choose")
        print("1:\tLearn Python")
        print("2:\tLearn java")
        print("3:\tGo Swimming")
        print("0:\tExit")
    choice = input()

