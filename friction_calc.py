#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 19, 2025
# This program calculates the static or
# kinetic friction given the friction type,
# coefficient of friction, and normal force.

# Import the constants module for useful constants.
import constants


# Define a function to calculate the resulting frictional force.
def calculate_friction(friction_coefficient, normal_force):
    # Simply return the product of the friction
    # coefficient and the normal force.
    return friction_coefficient * normal_force


# Define the main function.
def main():
    # Display the greeting message to the user.
    print(
        f"\n{constants.LIGHT_GREEN}Hello, user! This program will calculate the frictional "
        f"force based on the entered static or kinetic coefficient of friction and normal force."
        f"{constants.WHITE}\n"
    )

    # Construct an infinite while loop.
    while True:
        # Get the friction type from the user,
        # which can be static or kinetic.
        user_frict_type = input(
            f"{constants.LIGHT_BLUE}Enter the "
            f"friction type (static or kinetic): {constants.WHITE}"
        )

        # Check if the user entered static or
        # kinetic, regardless of letter case.
        if (user_frict_type.lower() == "static") or (
            user_frict_type.lower() == "kinetic"
        ):
            # Break out of the infinite loop
            # to simulate a do..while loop.
            break
        else:
            # Otherwise, notify the user that they entered an
            # unrecognized friction type and that they must try again.
            print(
                f"\n{constants.LIGHT_RED}{user_frict_type} is not a recognized "
                f"type of friction. Please try again.{constants.WHITE}\n"
            )

    # Construct another infinite while loop.
    while True:
        # Get the friction coefficient from the user as a string.
        user_frict_coefficient_str = input(
            f"\n{constants.LIGHT_PURPLE}Enter the coefficient "
            f"of friction (dimensionless): {constants.WHITE}"
        )

        # Try to validate and proceed with the friction coefficient input.
        try:
            # Attempt to convert the entered string into a float.
            user_frict_coefficient_float = float(user_frict_coefficient_str)

            # Check if the friction coefficient float is negative. Also, look
            # for the weird -0 exception and assume it is negative for safety.
            if (user_frict_coefficient_float < 0) or (
                user_frict_coefficient_str[0] == "-"
            ):
                # Notify the user that the coefficient of friction
                # cannot be negative and that they must try again.
                print(
                    f"\n{constants.LIGHT_RED}Coefficient of friction "
                    f"cannot be negative. Please try again.{constants.WHITE}"
                )
            # Otherwise, the friction coefficient is positive.
            else:
                # Nest another infinite while loop for the successive input.
                while True:
                    # Get the normal force from the user as a string.
                    user_normal_force_str = input(
                        f"\n{constants.LIGHT_CYAN}Enter the "
                        f"normal force (N): {constants.WHITE}"
                    )

                    # Try to validate and proceed with the normal force input.
                    try:
                        # Attempt to convert the entered string into a float.
                        user_normal_force_float = float(user_normal_force_str)

                        # Check if the normal force float is negative.
                        # Look for the same -0 exception for safety.
                        if (user_normal_force_float < 0) or (
                            user_normal_force_str[0] == "-"
                        ):
                            # Notify the user that the normal force cannot
                            # be negative and that they must try again.
                            print(
                                f"\n{constants.LIGHT_RED}Normal force cannot "
                                f"be negative. Please try again.{constants.WHITE}"
                            )
                        # Otherwise, the normal force is positive.
                        else:
                            # Break out of the inner infinite while loop.
                            break
                    # Runs if float() cannot convert the user's
                    # normal force input into a float.
                    except:
                        # Notify the user that they entered an
                        # invalid number for the normal force.
                        print(
                            f"\n{constants.LIGHT_RED}{user_normal_force_str} is "
                            f"not a valid number. Please try again.{constants.WHITE}"
                        )
                # Break out of the outer infinite while loop.
                break
        # Runs if float() cannot convert the user's
        # friction coefficient input into a float.
        except:
            # Notify the user that they entered an invalid
            # number for the friction coefficient.
            print(
                f"\n{constants.LIGHT_RED}{user_frict_coefficient_str} is "
                f"not a valid number. Please try again.{constants.WHITE}"
            )

    # Determine the friction result by assigning it
    # to the function with the validated user inputs.
    friction_result = calculate_friction(
        user_frict_coefficient_float, user_normal_force_float
    )

    # Finally, display the type of friction with information
    # and the resulting value, rounded to two decimal places.
    print(
        f"\n{constants.DARK_GRAY}The resulting "
        f"{constants.FRICTION_INFO[user_frict_type.lower()]} "
        f"is {friction_result:.2f} N.{constants.WHITE}\n"
    )


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
