
dic_label_num = dict() #dictionary: key is label name, value is label No
dic_exp_label = dict() #dictionary: key is exp No, value is label name

def init_dic_label():
    filename = "E-TABM-185.sdrf.txt"
    lines = open(filename).read().split('\n')
    label_num = 1
    for i in range(1, len(lines)):
        segment = lines[i].split('\t')
        if(len(segment) < 30): continue
        value = segment[29] #Factor Value [ORGANISMPART]
        if (value not in dic_label_num):
            dic_label_num[value] = label_num
            label_num += 1
        dic_exp_label[i] = value

if __name__ == '__main__':
    init_dic_label()


