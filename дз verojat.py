import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as pit
import matplotlib.mlab as mlab

x = np.random.rand(100)
num_bins = 10
n, bins, patches = plt.hist(x, num_bins)
plt.xlabel('x')
plt.ylabel('probability')
plt.title('histogram')
plt.show()