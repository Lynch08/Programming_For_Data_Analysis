# First Histogram Plot
#Author Enda Lynch
# Resources used : https://web.microsoftstream.com/video/b88a8cbb-2dbd-4cc2-835c-46101baed276

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0.0, 1.0, 1000)


plt.hist(x, bins = 100)
plt.show()



