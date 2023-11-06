from drink import Coco, Coffee

def make_drink(drink_type):
    if drink_type == "Coco":
        drink = Coco()

    elif drink_type == "Coffee":
        drink = Coffee()

    else:
        raise ValueError("Unsupported drink type")

    print(f"Making a {drink_type} drink:")
    drink.prepare()
    print("Drink is ready!")

if __name__ == "__main__":
    drink_type = input("Enter the type of drink (Coco or Coffee): ")
    make_drink(drink_type)