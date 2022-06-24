import numpy as np
from scipy import stats
arr =[54,12,45,61,52,45,45,67,34,56,78,32,56,40]
#to calculate mean
mean = np.mean(arr)
print("mean",mean)
#to median
median = np.median(arr)
print("median ",median)
# for mode
mode = stats.mode(arr)
print("mode ",mode)

#for standard deviation
std = np.std(arr)
print("deviation :",std)

#variance
var = np.var(arr)
print("varinace ",var)

print("cross checking std ",var**0.5)