def kg_to_pound(kg):
    return (kg * 0.45)

def pound_to_kg(pound):
    return (pound * 2.205)

if __name__ == "__main__":
    value = float(input("Enter your weight: "))
    unit = input("Enter your unit (k: kilogram / l: pound): ")
    if unit == "k" or unit == "kilogram":
        value = kg_to_pound(value)
        print (f"{value} pound")
    elif unit == "l" or unit == "pound":
        value = pound_to_kg(value)
        print(f"{value} kg")
    else:
        print(f"{unit} not valid")

        