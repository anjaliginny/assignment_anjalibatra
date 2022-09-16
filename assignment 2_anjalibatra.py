import statistics as stats
import numpy as np

li = np.array([1,33,5,14,69,45,84,2])

# mean of data
print(f"mean of given data is: {stats.mean(li)}")
# median of data
print(f"median of given data is: {stats.median(li)}")
# standard deviation of data
print(f"median of given data is: {np.std(li)}")
# percentile of data
print(f"75th percentile of given data is: {np.percentile(li, 75)}")
