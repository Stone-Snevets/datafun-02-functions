"""
Purpose: Use functions found in Python's "math" module.
        Create simple custom function that uses simple math concepts.

Writen by Solomon Stevens

Uses math module for advanced mathamatical functions

"""

#Import math function
import math

#Import logger setup information
from util_logger import setup_logger
logger, logname = setup_logger(__file__)

#Define custom functions
def get_area_of_car_wheel(radius):
    return math.pi * (radius ** 2)

def miles_per_kilowatt(miles_per_charge, total_kilowatts):
    return total_kilowatts / miles_per_charge

def electric_car_annual_spendings(amount_per_charge, miles_per_charge, miles_travelled_per_year):
    return amount_per_charge * miles_per_charge * miles_travelled_per_year
#$11 per charge 15,000 miles per year @300 miles per full charge


#Paste logger code for permutations and combinations
if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info(f"math.pi = {math.pi}")
    logger.info(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    logger.info(f"math.radians(180)         = {math.radians(180)}")
    logger.info("")
    logger.info(f"===== Calculating Area of Car Wheel =====")
    logger.info(f"Area for wheel with radius of 30 inches = {get_area_of_car_wheel(30)} square inches.")
    logger.info(f"Area for wheel with radius of 32 inches = {get_area_of_car_wheel(32)} square inches.")
    logger.info(f"Area for wheel with radius of 24 inches = {get_area_of_car_wheel(24)} square inches.")
    logger.info(f"Area for wheel with radius of 38 inches = {get_area_of_car_wheel(38)} square inches.")
    logger.info(f"===== Other Simple Functions =====")
    logger.info(f"math.fabs(-23) = {math.fabs(-23)}.")
    logger.info(f"The kilowatt efficiency of a car that can hold 60 kilowatt hours and can run 257 miles on a full charge is {miles_per_kilowatt(257, 60)} miles per kilowatt hour.")
    logger.info(f"If a person were to travel 15,000 miles in a year in a car that can go 300 miles in a full charge,")
    logger.info(f"...they would need to charge their car approximately {15000/300} times.  At $11 per full charge, they would pay ${11*(15000/300)} per year.")
    

