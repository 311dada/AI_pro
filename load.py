import numpy as np

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

