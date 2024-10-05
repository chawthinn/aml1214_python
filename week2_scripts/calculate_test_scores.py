# This program calculates test scores for students

# Define function
def cal_test_score():

    # Initialize variables
    total_score = 0
    average_score = 0

    # Get values
    print("The Test Scores program")
    print()
    print("Enter 3 test scores")
    print("===========================")
    for _ in range(3):
        total_score += int(input("Enter test score:\t"))

    # Calculate results
    average_score = round(total_score / 3)

    # Print results
    print("===========================")
    print("Total Score:\t\t" + str(total_score) +
    "\nAverage Score:\t\t" + str(average_score))
    print("\nBye")
