"""

Purpose: Illustrate the built-in statistics module on multivariate data.

VS Code Menu / View / Command Palette / Python Interpreter
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules.

@ uses statistics module for descriptive stats
@ uses sys module for checking Python version

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------


# Import from Python Standard Library

import statistics
import sys

#Bivariant data (I just used a random number generator for the numbers)
numUnnecessaryFeatures = [8, 5, 3, 6, 7, 4, 9, 10]
milesPerCharge = [182, 345, 372, 288, 261, 371, 138, 129]

# Stats for first variable
logger.info(f"===== Statistics for number of unnecessary features in an electric car =====")

# Descriptive: Averages and measures of central tendency
meanX = statistics.mean(numUnnecessaryFeatures)
medianX = statistics.median(numUnnecessaryFeatures)
modeX = statistics.mode(numUnnecessaryFeatures)


# Descriptive: Measures of spread
varX = statistics.variance(numUnnecessaryFeatures)
stdevX = statistics.stdev(numUnnecessaryFeatures)
lowestX = min(numUnnecessaryFeatures)
highestX = max(numUnnecessaryFeatures)


# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean    =   {meanX:.2f} features")
logger.info(f"median  =   {medianX:.2f} features")
logger.info(f"mode    =   {modeX:.2f} features")
logger.info(f"var     =   {varX:.2f} features")
logger.info(f"stdev   =   {stdevX:.2f} features")
logger.info(f"lowest  =   {lowestX:.2f} features")
logger.info(f"highest =   {highestX:.2f} features")
logger.info(f"range   =   {highestX-lowestX:.2f} features")
logger.info("")# newline



# Stats for second variable
logger.info(f"===== Statistics for miles an electric car can travel in a full charge =====")

# Descriptive: Averages and measures of central tendency
meanY = statistics.mean(milesPerCharge)
medianY = statistics.median(milesPerCharge)
modeY = statistics.mode(milesPerCharge)


# Descriptive: Measures of spread
varY = statistics.variance(milesPerCharge)
stdevY = statistics.stdev(milesPerCharge)
lowestY = min(milesPerCharge)
highestY = max(milesPerCharge)


# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean    =   {meanY:.2f} miles per full charge")
logger.info(f"median  =   {medianY:.2f} miles per full charge")
logger.info(f"mode    =   {modeY:.2f} miles per full charge")
logger.info(f"var     =   {varY:.2f} miles per full charge")
logger.info(f"stdev   =   {stdevY:.2f} miles per full charge")
logger.info(f"lowest  =   {lowestY:.2f} miles per full charge")
logger.info(f"highest =   {highestY:.2f} miles per full charge")
logger.info(f"range   =   {highestY-lowestY:.2f} miles per full charge")
logger.info("")# newline

# Call linear_regression() function -
# and get back 2 values: slope and intercept
# describing the 'best fit' line through the data
slope, intercept = statistics.linear_regression(numUnnecessaryFeatures, milesPerCharge)

# Choose an x value off in the future (future x)
future_x = 11

# Extend the line out into the unknown future
# and read the value (of future y)
future_y = round(slope * future_x + intercept)

logger.info("Here's some bivariant data (2 variables, together):")
logger.info(f"x:{numUnnecessaryFeatures}")
logger.info(f"y:{milesPerCharge}")
logger.info("Calculate the slope and intercept of a best fit straight line:")
logger.info(f"   slope = {slope:.2f}")
logger.info(f"   intercept = { intercept:.2f}")
logger.info("Let's use our best fit line to PREDICT a future value.")
logger.info(f"   At future x = {future_x:d} features,")
logger.info(f"   we predict the value of y will be { future_y:d} miles per full charge.")
logger.info("How'd we do? Does this make sense given the data?")
