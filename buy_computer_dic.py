computer_parts = {
    "1": "monitor",
    "2": "mouse",
    "3": "hdmi cabel",
    "4": "SSD",
}

current_choice = None
# list
buy_parts = []

# dictionary
buy_parts_dic = {}

while current_choice != "0":
    if current_choice in computer_parts:
        chosen_part = computer_parts[current_choice]
        # dictionary
        if current_choice in buy_parts_dic:
            print(f"remove {chosen_part}")
            buy_parts_dic.pop(current_choice)
        else:
            print(f"adding {chosen_part}")
            buy_parts_dic[current_choice] = chosen_part
        print(f"Youre dictionary now contains: {buy_parts_dic}")
        # list
        # if chosen_part in buy_parts:
        #     print(f"remove {chosen_part}")
        #     buy_parts.remove(chosen_part)
        # else:
        #     print(f"adding {chosen_part}")
        #     buy_parts.append(chosen_part)
        # print(f"Youre list now contains: {buy_parts}")
    else:
        if current_choice == "10":
            print("add computer part:")
            key = input("please write number: ")
            value = input("please write value: ")
            computer_parts[key] = value  
        print("Please add option form the list")
        for key, value in computer_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")  

    current_choice = input("> ")