'''

Histogram:

    A histogram is a graph showing frequency distributions.

    It is a graph showing the number of observations within each given interval.

    Example: Say you ask for the height of 250 people, you might end up with a histogram like this:


    A Histogram is a diagrammatic representation of a group of data over user-specified ranges.
    Basically, the histogram contains several bins. Bins are non-overlapping intervals in which the data is spread.
    In MATLAB we have a function named hist() which allows us to plot a bar graph

    Syntax:

    hist(X)
    where X represents the data. The X is a vector.
'''
#simple Histogram

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()



# y = np.array([35, 25, 25, 15])
#
# plt.pie(y)
# plt.show()