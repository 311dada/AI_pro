import numpy as np

# x is a 2-dimention list
#k is the output dimention
#the output is a low-dimention numpy array
 
def PCA(x,k):
  print ('PCA is starting!')
  X = np.array(x)
  X = X - np.mean(X,axis = 1,keepdims = True)
  m = X.shape[1]
  C = 1.0/m*np.dot(X,X.T)
  e,ev = np.linalg.eigh(C)
  ev = ev[::-1]
  Y = np.dot(ev,X)
  Y = Y[::k]
  f = open('PCA.txt','w')
  for i in range(Y.shape[0]):
     for j in range(Y.shape[1]):
       f.write(str(Y[i][j])+' ')
     f.write('\n')  
  f.close() 
  print ('PCA has finished!')
 




