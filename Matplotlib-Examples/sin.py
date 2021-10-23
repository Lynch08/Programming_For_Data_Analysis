# sin and cos plots
#Author Enda Lynch
# Resources used : https://web.microsoftstream.com/video/8f09d1fe-9b94-4908-b71e-94ed7b119174

import matplotlib.pyplot as plt
import numpy as np

x= np.arange (-2.0 * np.pi, 2.0 * np.pi, 0.1)

plt.plot(x, np.sin(x), 'g.')
plt.plot(x, np.cos(x), 'b.')

plt.show()