import numpy as np




dic_label_num = dict() #dictionary: key is label name, value is label No
dic_num_label = dict() #the opposite
dic_label_num['BLANK'] = 0
dic_num_label[0] = 'BLANK'
def init_dic_label():
    filename = "E-TABM-185.sdrf.txt"
    lines = open(filename).read().strip().split('\n')
    label_num = 1
    y = [0 for i in range(5896)]
    for i in range(1, len(lines)):
        segment = lines[i].split('\t')
        if(len(segment) < 30): 
            value = 'BLANK'
        else: value = segment[29] #Factor Value [ORGANISMPART]
        if (value not in dic_label_num):
            dic_label_num[value] = label_num
            dic_num_label[label_num] = value
            label_num += 1
        y[i-1] = dic_label_num[value]
    print ('the labeling has finished!')
    return y

new_label2id = dict()
new_id2label = dict()

def select(x,y):
  times = dict()
  for i in y:
    if i not in times:
       times[i] = 1
    else: times[i] += 1
  z = []
  pos = []
  new_label=[]
  new_num = 0
  for num in times:
    if times[num]>=10:
       z.append(num)
  print (len(z))
  for i in range(5896):
     if y[i] in z:
        pos.append(i)
        value = dic_num_label[y[i]]
        if value not in new_label2id:
           new_label2id[value] = new_num
           new_id2label[new_num] = value
           new_num += 1
        new_label.append(new_label2id[value])
  new_x = x[:,np.array(pos)]
  np.save('final.npy',new_x)
  np.save('label.npy',np.array(new_label))

x = np.load('new_data.npy')
y = init_dic_label()
select(x,y)
