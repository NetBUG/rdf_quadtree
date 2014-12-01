import numpy as np
import matplotlib.pyplot as plt
import pyqtree

np.random.seed(5)
x = np.arange(1, 101)
y = 20 + 3 * x + np.random.normal(0, 60, 100)
plt.plot(x, y, "o")

plt.plot([50, 150], [100, 100], 'k-', lw=2)	# draw vertical line from (70,100) to (70, 250)
#plt.plot([100, 200], [300, 200], 'k-')		# draw diagonal line from (70, 90) to (90, 200)
plt.show()
