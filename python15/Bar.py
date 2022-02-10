'''
Matplotlib Bars:
   A bar plot or bar chart is a graph that represents the category of data with rectangular bars with
   lengths and heights that is proportional to the values which they represent. The bar plots can be
   plotted horizontally or vertically. A bar chart describes the comparisons between the discrete categories.
    One of the axis of the plot represents the specific categories being
   compared, while the other axis represents the measured values corresponding to those categories.


    Creating a bar plot:
    The matplotlib API in Python provides the bar() function which can be used in MATLAB style use or
    as an object-oriented API. The syntax of the bar() function to be used with the axes is as follows:-

    plt.bar(x, height, width, bottom, align)


    jhbfbvjhvbjhb fjhsbjh v jbvlv a 

'''

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 15])

plt.bar(x,y)
plt.show()

x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x, y,color = "red" ,width = 0.1)
plt.show()

'''
Horizontal Bars
If you want the bars to be displayed horizontally instead of vertically, use the barh() function:

'''

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()


