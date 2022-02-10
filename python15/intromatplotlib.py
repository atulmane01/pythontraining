'''

What is Matplotlib?
     Matplotlib is an amazing visualization library in Python for 2D plots of arrays. Matplotlib is a multi-platform
     data visualization library built on NumPy arrays and designed to work with the broader SciPy stack. It was
     introduced by John Hunter in the year 2002.

    One of the greatest benefits of visualization is that it allows us visual access to huge amounts of data in easily
    digestible visuals. Matplotlib consists of several plots like line, bar, scatter, histogram etc.

    Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

    Matplotlib was created by John D. Hunter.

    Matplotlib is open source and we can use it freely.

    Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.
'''
import matplotlib.pyplot as plt


x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 2]

plt.plot(x, y)
plt.show()
