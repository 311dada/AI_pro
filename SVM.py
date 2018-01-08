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
  n = ev.shape[0]
  ev = ev[::-1]
  P = ev[np.arange(k),:]
  Y = np.dot(P,X)
  f = open('PCA.txt','w')
  for i in range(Y.shape[0]):
     for j in range(Y.shape[1]):
       f.write(str(Y[i][j])+' ')
     f.write('\n')  
  f.close() 
  print ('PCA has finished!')
  return Y

#load the raw data as a matrix

def load_raw_data():
  f = open('microarray.original.txt','r')
  content = f.readline()
  data = [[] for i in range(22282)]
  k = 0
  content = f.readline()
  while True:
    content = f.readline()
    if content =='':
       break
    content = content.strip().split('\t')
    del content[0]
    for i in content:
      data[k].append(float(i))
    k = k + 1
    if k%1000==0:
       print (str(float(k)/22282)+'%')
  print ("the data has been loaded completely!")
  f.close()
  return data


dic_label_num = dict() #dictionary: key is label name, value is label No
dic_exp_label = dict() #dictionary: key is exp No, value is label name

def init_dic_label():
    filename = "E-TABM-185.sdrf.txt"
    lines = open(filename).read().split('\n')
    label_num = 0
    y = np.array([0 for i in range(5896)])
    for i in range(1, len(lines)):
        segment = lines[i].split('\t')
        if(len(segment) < 30): continue
        value = segment[29] #Factor Value [ORGANISMPART]
        if (value not in dic_label_num):
            dic_label_num[value] = label_num
            label_num += 1
        dic_exp_label[i-1] = value
        y[i-1] = dic_label_num[value]
    print ('the labeling has finished!')
    return y

x = load_raw_data()
X_raw = PCA(x,5000).T
init_dic_label()  
y_raw = init_dic_label()   


