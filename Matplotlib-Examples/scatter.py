# scatter plots
#Author Enda Lynch
# Resources used : https://web.microsoftstream.com/video/8f09d1fe-9b94-4908-b71e-94ed7b119174

import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(0.0, 10.0, 100)
y = np.random.uniform(0.0, 100.0, 100)
z = np.random.normal(100.0, 40.0, 100)
c = np.random.randint(0, 20, 100)

plt.scatter(x, y, c=c, s=z)
plt.show()