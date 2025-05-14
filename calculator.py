#!/usr/bin/env python3
# Created By: Chanella
# Date: May 14, 2025
# Write what this program does.


def result_num(num_1, num_2, operator_str):
    # This function takes two numbers and an operator as input
    # and returns the result of the operation
    if operator_str == "+":
        return num_1 + num_2
    elif operator_str == "-":
        return num_1 - num_2
    elif operator_str == "*":
        return num_1 * num_2
    elif operator_str == "/":
        return num_1 / num_2
    elif operator_str == "%":
        return num_1 % num_2


def main():
    user_num_1 = 0
    user_num_2 = 0
    operator_str = 0
    try:
        # This function takes user input for two numbers and an operator
        # and prints the result of the operation
        user_num_1 = float(input("Enter the first number: "))
        user_num_2 = float(input("Enter the second number: "))
        operator_str = input("Enter the operator (+,-,*./,%) : ")
        print("")

        if (
            operator_str == "+"
            or operator_str == "-"
            or operator_str == "*"
            or operator_str == "/"
            or operator_str == "%"
        ):
            result = result_num(user_num_1, user_num_2, operator_str)
            print(result)

    except:
        print("Invalid!")


if __name__ == "__main__":
    main()
