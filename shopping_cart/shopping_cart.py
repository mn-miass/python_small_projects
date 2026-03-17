if __name__ == "__main__":

    foods = {}
    prices = []
    total = 0

    while True:
        food = input("Enter the food to buy(q to quit): ")
        flag = 0
        if food == 'q':
            break
        else :
            for item in foods.keys():
                if item == food:
                    total += foods[food]
                    print(f"Item {food} was added succesfully : {foods[food]}")
                    flag = 1
            if flag == 0:
                price = input("Enter the element price: ")
                try:
                    foods[food] = int(price)
                    print(f"Item {food} was added succesfully : {foods[food]}")
                    total += foods[food]
                except:
                    print("invalid price was given")
    print("====Your Cart====")
    for food in foods.keys():
        print(f"food: {food}   price: {foods[food]}")
    print(f"The total is {total}")
