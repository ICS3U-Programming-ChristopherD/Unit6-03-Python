#!/usr/bin/env python3

# Created by: Chris Di Bert
# Date: Dec.15, 2022
# This program generates 10 random numbers and
# prints the largest number

import random
import constants


def min_value(number_list):

    # Sets lowest number to a number greater than 100
    # so that any new number generated will replace it
    lowest_number = 101

    # Gets the largest number by comparing previous largest numbers
    for counter in number_list:
        if counter < lowest_number:
            lowest_number = counter

    # Returns the lowest number
    return lowest_number


def main():
    # Creates an empty list for the random numbers
    random_numbers = []

    # For loop generates ten random numbers from 1-100
    for counter in range(constants.MAX_ARRAY_SIZE):

        # Generates random number from 1-100
        random_int = random.randint(constants.MIN_NUM, constants.MAX_NUM)

        # Adds random number to list
        random_numbers.append(random_int)

        print(f"Added {random_int} to list at index {counter}")

    # Stores largest number generated in variable
    smallest_value = min_value(random_numbers)

    # Prints the largest number generated
    print(f"The lowest value is: {smallest_value}.")


if __name__ == "__main__":
    main()
