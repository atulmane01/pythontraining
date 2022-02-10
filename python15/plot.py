'''

How to create Plot:
    This series will introduce you to graphing in python with Matplotlib, which is arguably the most popular graphing and data visualization library for Python.
Installation
The easiest way to install matplotlib is to use pip. Type following command in terminal:

pip install matplotlib
'''

# importing the required module
import matplotlib.pyplot as plt
from matplotlib import style
plt.style.use("ggplot")
# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()

'''
The code seems self-explanatory. Following steps were followed: 

Define the x-axis and corresponding y-axis values as lists.
Plot them on canvas using .plot() function.
Give a name to x-axis and y-axis using .xlabel() and .ylabel() functions.
Give a title to your plot using .title() function.
Finally, to view your plot, we use .show() function.

'''

#Plotting two or more lines on same plot

import matplotlib.pyplot as plt

# line 1 points
x1 = [1,2,3]
y1 = [2,4,1]
# plotting the line 1 points
plt.plot(x1, y1, label = "line 1")

# line 2 points
x2 = [1,2,3]
y2 = [4,1,3]
# plotting the line 2 points
plt.plot(x2, y2, label = "line 2")

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()

