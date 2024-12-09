# This program calculates miles per gallon
# based on the input given by the user

# Define function
def cal_mile_per_gallon():

    # Initialize variables
    total_miles = 0
    total_gallons = 0
    miles_per_gallon = 0

    # Get values
    print("The Miles Per Gallon program")
    print()
    total_miles = float(input("Enter miles driven:\t\t"))
    total_gallons = float(input("Enter gallons of gas used:\t"))

    # Calculate miles per gallon
    miles_per_gallon = total_miles/total_gallons

    # Print result
    print()
    print("Miles Per Gallon:\t\t" + str(round(miles_per_gallon,2)))
    print()
    print("Bye")
