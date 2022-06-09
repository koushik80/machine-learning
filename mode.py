#Mode:
#The Mode value is the value that appears the most number of times:

#99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86 = 86

#The SciPy module has a method for this.

#Example
#Use the SciPy mode() method to find the number that appears the most:


from scipy import stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

x = stats.mode(speed)

print(x)
