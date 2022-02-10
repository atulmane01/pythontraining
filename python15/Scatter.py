'''

How to create Scatter:
    Creating Scatter Plots
    With Pyplot, you can use the scatter() function to draw a scatter plot.

    The scatter() function plots one dot for each observation. It needs two arrays of the same length,
     one for the values of the x-axis, and one for values on the y-axis:



'''
#A simple scatter plot:


import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y,color = '#88c999',alpha=0.5)
plt.show()


#drawaing two scatter plot into the same figure

import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y )

plt.show()