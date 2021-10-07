# First 2d plot
#Author Enda Lynch
# Resources used : https://web.microsoftstream.com/video/204cd80b-2054-4587-9a9a-33020e84ba56

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0
noise = np.random.normal(0.0, 1.0, len(x))




plt.plot (x, y + noise, 'r.')
plt.plot (x, y, 'b-')

plt.show()

plt.plot (x, y + noise, 'c.')
plt.plot (x, y, 'g-')

plt.show()