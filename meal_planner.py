import dis
from secrets import choice
from socket import setdefaulttimeout
from contents import pantry, recipes

def add_shopping_item(data: dict, item: str, amout: int) ->None:
    """
    add a tuple containing `item` and `amout` to the `data` dict.
    """
    # if item in data:
    #     data[item] += amout
    # else:
    #     data[item] = amout

    # შემოკლებული ვარიანტი setdefault ამოწმებს გასაღები არსებობს თუ არა თუ არ არსებობს ქმნის 
    data[item] = data.setdefault(item, 0) + amout

display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}

while True:
    print('Please choose youre recipe')
    print("--------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"Youre have selected {selected_item}")
        print("Checking ingredients.....")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy: {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

for things in shopping_list.items():
    print(things)
