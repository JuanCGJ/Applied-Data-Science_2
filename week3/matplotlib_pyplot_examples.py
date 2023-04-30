import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create just a figure and only one subplot
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title('Simple plot')
# plt.show()

#Create two subplots and unpack the output array immediately
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)
plt.show()

# Create four polar axes and access them through the returned array
# fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
# axs[0, 0].plot(x, y)
# axs[1, 1].scatter(x, y)
# plt.show()

# Share a X axis with each column of subplots
# plt.subplots(2, 2, sharex='col')
# plt.show()

# Share a Y axis with each row of subplots
# plt.subplots(2, 2, sharey='row')
# plt.show()

# Share both X and Y axes with all subplots
# plt.subplots(2, 2, sharex='all', sharey='all')
# plt.show()

# Note that this is the same as
# plt.subplots(2, 2, sharex=True, sharey=True)
# plt.show()

# Create figure number 10 with a single subplot
# and clears it if it already exists.
# fig, ax = plt.subplots(num=10, clear=True)
# plt.show()
