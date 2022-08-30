current_chose = "-"
computer_parts = []
avalable_partes = ["monitor",
                   "keyboard",
                   "mouse",
                   "computer",
                   ]
# valid_chose = [str(i) for i in range(1, len(avalable_partes) +1)]
valide_chose = []
for i in range(1, len(avalable_partes) +1):
    valide_chose.append(str(i))
while current_chose != "0":
    if current_chose in "1234":
        index = int(current_chose) - 1
        chosen_part = avalable_partes[index]
        if chosen_part in computer_parts:
            print("remove {}".format(current_chose))
            computer_parts.remove(chosen_part)
        else:
            print("adding {}".format(current_chose))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("please add")
        for number, part in enumerate(avalable_partes):
            print("{0}: {1}".format(number, part))
    current_chose = input()
print(computer_parts)


