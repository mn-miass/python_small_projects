def celsius_to_fahrnheit(celsius):
    return ((9 * celsius) / 5 + 32)

def fahrnheit_to_celsius(fahrnheit):
    return ((fahrnheit - 32) * 5 / 9)

if __name__ == "__main__":
    unit = input("Enter the valid temperture unit (C/F): ")
    if unit == "F":
        value = float(input("Enter the temperturein in fahrenheit: "))
        value = fahrnheit_to_celsius(value)
        print(f"{round(value, 2)} in celsius")
    elif unit == "C":
        value = float(input("Enter the temperturein in celsius: "))
        value = celsius_to_fahrnheit(value)
        print(f"{round(value, 2)} in fahrenheit")
    else:
        print(f"{unit} is invalid")
        exit()
