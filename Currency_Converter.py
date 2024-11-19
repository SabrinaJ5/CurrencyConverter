"""
Author: Sabrina Joseph
Date: 01-24-2024
Last Modified: 01-24-2024
Description: Module 2 Lab Activity C
"""

print("Available currencies: A)USD B)CAD C)YEN")
amount = float(input("Enter transaction amount: "))
original = input("Transaction currency: ")
conversion = input("Currency to convert to: ")

# if the original amount is in USD
if original == "A" or original == "a":
    # USD to CAD
    if conversion == "B" or conversion == "b":
        amount *= 1.24
        print(f"Converted value: {round(amount, 2)} CAD")
    # USD to YEN
    elif conversion == "C" or conversion == "c":
        amount *= 108.59
        print(f"Converted value: {round(amount, 2)} YEN")
    elif conversion == "A" or conversion == "a":
        print("Conversion not needed...")

# if the original amount is in CAD
elif original == "B" or original == "b":
    # CAD to USD
    if conversion == "A" or conversion == "a":
        amount /= 1.24
        print(f"Converted value: {round(amount, 2)} USD")
    # CAD to YEN
    elif conversion == "C" or conversion == "c":
        amount /= 1.24
        amount *= 108.59
        print(f"Converted value: {round(amount, 2)} YEN")
    else:
        print("Conversion not needed...")

# if the original amount is in Yen
elif original == "C" or original == "c":
    # YEN to USD
    if conversion == "A" or conversion == "a":
        amount /= 108.59
        print(f"Converted value: {round(amount, 2)} USD")
    # YEN to CAD
    elif conversion == "B" or conversion == "b":
        amount /= 108.59
        amount *= 1.24
        print(f"Converted value: {round(amount, 2)} CAD")
    else:
        print("Conversion not needed...")
