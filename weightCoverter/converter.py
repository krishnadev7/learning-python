print()
print("Weight Converter")
print()
weight = float(input("Enter your weight: "))
weight_input = input("(L)bs or (K)g: ").lower()

if weight_input == "k":
    pounds = weight * 2.205
    print(f"You are {pounds} pounds")
elif weight_input == "l":
    kilo = weight / 2.205
    print(f"You are {kilo} kilograms")
else:
    print("Invalid input enter L for pounds and K for kilograms")