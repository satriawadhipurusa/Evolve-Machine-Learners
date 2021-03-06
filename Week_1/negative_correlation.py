import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(1)
matplotlib.style.use('ggplot')

# 1000 random integers between 0 and 50
x = np.random.randint(0, 50, 1000)

# Negative Correlation with some noise
y = 100-(x + np.random.normal(0, 10, 1000))

corrcoeffs=stats.spearmanr(x, y)
print("corrcoeffs:")
print(corrcoeffs)

plt.scatter(x, y)
plt.show()