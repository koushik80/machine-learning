#Median:
#The median value is the value in the middle, after you have sorted all the values:

#77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111

#It is important that the numbers are sorted before you can find the median.

#The NumPy module has a method for this:

#Example
#Use the NumPy median() method to find the middle value:

import numpy

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = numpy.median(speed)

print(x)

#**If there are two numbers in the middle, divide the sum of those numbers by two.

#77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103

#(86 + 87) / 2 = 86.5
