#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 19, 2025
# This program calculates the static or
# kinetic friction given the friction type,
# coefficient of friction, and normal force.

# Import the constants module for useful constants.
import constants


# Define a function to calculate the
# resulting frictional force.
def calculate_friction(friction_coefficient, normal_force):
    # Simply return the product of the friction
    # coefficient and the normal force.
    return friction_coefficient * normal_force


# Define the main function.
def main():
    # Display the greeting message to the user.
    print(f"\n{constants.LIGHT_GREEN}Hello, user! This program will calculate the frictional "
    f"force based on the entered static or kinetic coefficient of friction and normal force."
    f"{constants.WHITE}\n")

    # Construct an infinite while loop.
    while True:
        # Get the friction type from the user,
        # which can be static or kinetic.
        user_frict_type = input("Enter the friction type (static or kinetic): ")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
