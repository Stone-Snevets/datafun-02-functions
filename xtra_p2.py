"""
Purpose: 

Practice writing functions using positional and keyword arguments.
Practice logging functions using the util_datafun_logger module
Log each time the function is called (along with its arguments)
Log the result of each function just before you return the result

 ----------------------------------------------------------
 UNIT TESTS BELOW - SPECIFY CORRECT BEHAVIOR
 ----------------------------------------------------------

>>> sum_two(1,2)
3

>>> sum_two("hello"," world")
'hello world'

>>> sum_rectangle_list( [1,1,3,3] )
8

>>> transform_using_keyword_args_with_default_values()
'bea'

>>> transform_using_keyword_args_with_default_values(reverse=True)
'aeb'

>>> transform_using_keyword_args_with_default_values(input="hello", reverse=True)
'leh'

>>> sum_any_using_args(1,1,1,2)
5

>>> sum_any_with_keyword_arguments_kwargs(a=1,b=2,c=3)
6

@uses doctest - to verify our functions are correct
"""

import doctest

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

# TODO: Add functions to get the unit tests to pass 
# TODO: Log each time the function is called (along with its arguments)
# TODO: Log the result of each function just before you return the result
def sum_two(first, second):
    """Return sum of two arguments"""

    logger.info(f"Calculating sum of {first} and {second}.")

    total = first + second

    logger.info(f"The sum of your arguments({first}, {second}) is {total}.")
    return total


def sum_rectangle_list(list):
    """Return sum of list of four numbers"""

    logger.info(f"Calculating the sum of the numbers {list}.")

    total = 0
    for n in list:
        total += n
    
    logger.info(f"The sum of the values {list} is {total}.")
    return total

def sum_any_using_args(*args):
    """Return sum of list of arguments"""

    logger.info(f"Calculating sum of list of arguments {args}.")

    #Initialize total to zero
    total = 0

    #Iterate through list of arguments
    for n in args:
        #add numbers in list of arguments
        total += n
    
    #Output and Return
    logger.info(f"The total sum of the list of arguments {args} is {total}.")
    return total

def sum_any_with_keyword_arguments_kwargs(a, b, c):
    '''Return sum of list of KEYWORD arguments'''

    logger.info(f"Calculating sum of list of keyword arguments {a}, {b}, {c}.")

    total = a + b + c
    
    logger.info(f"The sum of {a}, {b}, and {c} is {total}.")
    return total



# TODO: Fix this function to get just the first 3 letters (possibly reversed)
def transform_using_keyword_args_with_default_values(input="bearcat", reverse=False):
    '''Return a string with just the first 3 letters of input string. 
    If reverse is True, reverse the first 3 letters. 
    If reverse is omitted or False, return the first 3 letters reversed. 
    @kwargs:
        input: a string, default "bearcat"
        reverse: a boolean, default False'''
    
    s = f"CALLING transform_using_keyword_args_with_default_values(input={input}, reverse={reverse})"
    logger.info(s)

    #Obtain first 3 letters of input
    result = input[0:3:1]

    #Check if reversed
    if reverse:
        result = result[::-1]

    logger.info(f"RETURNING {result}")
    return result



if __name__ == "__main__":

    # -------------------------------------------------------------
    # Call some functions and execute code!
    # Nothing below here needs to change
    # -------------------------------------------------------------

    transform_using_keyword_args_with_default_values()
    transform_using_keyword_args_with_default_values(reverse=True)
    transform_using_keyword_args_with_default_values(input="hello", reverse=True)

    logger.info("===========================================================")
    logger.info("Running doctest.testmod() function to unit test our code")
    logger.info("===========================================================")

    # Run doctest and log the results

    doctest_result = doctest.testmod()
    if doctest_result.failed == 0:
        logger.info("All tests passed!")
    else:
        logger.error(f"{doctest_result.failed} tests failed!")

    logger.info("Script complete. More info in the log file.")
        
