'''
Purpose: Create a class that inherits everything from NumericSeries and adds
attributes and/or behavior specific to the milage of electric cars vs. gasoline cars. 

If you don't need to add specialized attributes or behavior, 
you can just use the original NumericSeries class directly. 
No subclassing required.

We get all of our parent's attributes and methods for free (no coding required).

This class adds:

- a location attribute (city trafic vs. highway trafic, etc.)
- a function coef_variance() to calculate the standard deviation relative to each mean

'''

#Import NumericSeries class
from numeric_series import NumericSeries

#Create Logger
from util_logger import setup_logger
logger, logname = setup_logger(__file__)


#Create the class
class NumericMilageSeries(NumericSeries):

    #Initializing function
    def __init__(self, name, units, data, location):
        """
        Initialize the object when first created using the arguments passed in.
        Every class needs an __init__ method to construct a new object.

        @args:
            self (object): the object being created that will hold the real data
            name (str): a short name for this list of numeric data
            units (str): the units in which the data is measured
            data (list): the list of numeric data to be held by the object
            location (str): the location where the data was collected

        """

        # First, initialize the parent (super) class with parent's attributes
        # By calling the super constructor method
        super().__init__(name, units, data)

        # Then, initialize our additional specialized attributes
        self.location = location


    # Create Custom Function
    def coef_variance(self):
        return self.standard_deviation() / self.mean()


    # Return Output
    def __str__(self):
        """
        Return a string representation of the instantiated object.
        The two underscores before and after indicate this is a special method.
        Every class needs a __str__ method that returns a string representation of the object.
        Be sure to use self.attribute_name so you use the object's attribute, not a local variable! 

        Returns:
            str: a string representation of the instantiated object
        """

        str = f"NumericMilageSeries with name= {self.name}, units= {self.units}, location= {self.location}, and {len(self.data)} data points: {self.data}"
        return str
    



# "Main" Function
if __name__ == "__main__":
    # If we're running this script (instead of using it in another class or script), 
    # Run some code to try our class

    # Create an object by calling the constructor 
    # The constructor method is always the name of the class
    # pass in the information required by the __init__ method defined in the class

    #-> Input 1
    name1 = "Electric SUV"
    units1 = "Miles / Charge"
    data1 = [132, 295, 322, 238, 211, 321, 88, 79]
    loc1 = "City Trafic"

    object1 = NumericMilageSeries(name1, units1, data1, loc1)

    #-> Input 2
    name2 = "Electric Car"
    units2 = "Miles / Charge"
    data2 = [182, 345, 372, 288, 261, 371, 138, 129]
    loc2 = "Suburban Trafic"

    object2 = NumericMilageSeries(name2, units2, data2, loc2)

    #-> Input 3
    name3 = "Gasoline Truck"
    units3 = "Miles / Gallon"
    data3 = [24, 33, 25, 32, 29, 30, 21, 22]
    loc3 = "Highway Trafic"

    object3 = NumericMilageSeries(name3, units3, data3, loc3)


    # Log the objects created
    logger.info(f"Created: {object1}")
    logger.info(f"Created: {object2}")
    logger.info(f"Created: {object3}")

    object_list = [object1, object2, object3]


    for object in object_list:
        logger.info("------------------")
        logger.info(object)
        logger.info(f"Count: {object.count()}")
        logger.info(f"Sum: {object.sum()}")
        logger.info(f"Mean: {object.mean()}")
        logger.info(f"Median: {object.median()}")
        logger.info(f"Variance: {object.variance():.2f}")
        logger.info(f"Standard Deviation: {object.standard_deviation():.2f}")
        logger.info(f"Coefficient of Variance: {object.coef_variance():.2f}")


