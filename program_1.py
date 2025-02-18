#Programmer: Timothy Pickering
#Date: 2/17/25
#Title: Basic Kilometer Converter

def kilometer_conversion(kilometers):
    miles = kilometers * 0.6214  #Convert kilometers to miles
    return miles  #Return the result

# Ask the user for input
kilometers = float(input("Please enter distance in kilometers: "))

# Call the function with the user input and print the result
print(f"Distance in miles: {kilometer_conversion(kilometers):.2f}")
