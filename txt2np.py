import numpy as np

f = open('PCA.txt','r')
x = np.zeros((5000,5896))
for i in range(5000):
   content = f.readline()
   content = content.strip().split()
   for j in range(5896):
     x[i][j] = float(content[j])
np.save('new_data.npy',x)
