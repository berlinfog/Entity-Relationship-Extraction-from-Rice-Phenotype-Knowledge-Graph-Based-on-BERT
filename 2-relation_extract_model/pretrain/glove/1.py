import numpy as np

loadData = np.load('vec.npy')

print("----type----")
print(type(loadData))
print("----shape----")
print(loadData.shape)
print("----data----")
print(loadData)