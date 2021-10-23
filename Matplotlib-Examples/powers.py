# To the power od plots
#Author Enda Lynch
# Resources used : https://web.microsoftstream.com/video/8f09d1fe-9b94-4908-b71e-94ed7b119174

import matplotlib.pyplot as plt
import numpy as np

x = np.arange (1.0, 100.0, 0.1)

plt.plot(x, x**2, 'g-', label='X^2')
plt.plot(x, x**3, 'b-', label='X^3')
plt.plot(x, x**4, 'r-', label='X^4')
plt.plot(x, 2**x, 'k-', label='2^X')

plt.legend()

plt.show()