#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: September 2019
# This program calculates the cost of the pizza


import constants


def main():

    # This function calculates the price of the pizza using the given size

    # input
    diameter = int(input("Enter the size of the pizza you want (inch): "))

    # process
    sub_total = constants.LABOR_COST + constants.RENT + \
        (diameter * constants.COST_PER_INCH)
    total = sub_total + (sub_total*constants.HST)

    # output
    print("")
    print("Your total for your pizza is ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
