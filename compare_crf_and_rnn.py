# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:12:01 2018

@author: Administrator
"""

import os
import os.path
import re
import numpy as np
import sys
import importlib
importlib.reload(sys)

PYTHONIOENCODING='utf-8'

## tags, BIEO
tag2label = {"N": 0,
             "B_bodyloc": 1, "I_bodyloc": 2,"E_bodyloc":3,
             "B_ZZ": 4, "I_ZZ": 5,"E_ZZ":6,
             "B_ZD": 7, "I_ZD": 8,"E_ZD":9,
             "B_JC": 10, "I_JC": 11,"E_JC":12,
             "B_ZL": 13, "I_ZL": 14,"E_ZL":15,
             "S_bodyloc":16,"S_ZZ": 17, "S_ZD": 18,"S_JC":19,"S_ZL":20

             }

label2tag = {"0": "N",
             '1': "B_bodyloc", '2':"I_bodyloc",'3':"E_bodyloc",
             '4':"B_ZZ", '5':"I_ZZ",'6':"E_ZZ",
             '7':"B_ZD", '8':"I_ZD",'9':"E_ZD",
             '10':"B_JC", '11':"I_JC",'12':"E_JC",
             '13':"B_ZL", '14':"I_ZL",'15':"E_ZL",
             '16':"S_bodyloc",'17':"S_ZZ", '18':"S_ZD",'19':"S_JC",'20':"S_ZL"

             }


file_path_crf = 'E:\\CCKS2017\\CRF++-0.58\\CRF++-0.58\\example\\my_train_ccks2017\\output1029.txt'
file_path_rnn = 'E:\\zh-NER-TF-master\\zh-NER-TF-master\\out.txt'
file_path = 'E:\\compare00.txt'

f = open(file_path_crf, 'r',encoding='utf-8')
crf_pre = f.read()
crf_pre = re.split('[\t\n]', crf_pre)
crf_pre = [n for n in crf_pre if n != '']  ##可以删除list中的所有空元素
crf_pre = np.array(crf_pre).reshape([-1,3])
#****
[crf_a, b, crf_c] = np.split(crf_pre, [1,2], axis=1)

key = 0
for i in crf_c:
    crf_c[key][0] = tag2label[i[0]]
    key = key + 1
#print(crf_c)
crf_c = crf_c.reshape([1,-1])[0]
crf_a = crf_a.reshape([1,-1])[0]

f.close()
f = open(file_path_rnn)
rnn_pre = f.read()
rnn_pre = rnn_pre.split('\n')
rnn_pre = [n for n in rnn_pre if n != '']  ##可以删除list中的所有空元素
key0=0
for i in rnn_pre:
    rnn_pre[key0]=label2tag[i]
    key0=key0+1
f.close()

rnn_pre = np.array(rnn_pre).reshape([-1,1])
#print(rnn_pre.shape())

out = np.append(crf_pre,rnn_pre,axis=1)
out[0][0]='1'
f= open(file_path,'w')
for i in out:
    for j in i:
        f.write(j)
        f.write('\t')
    f.write('\n')
f.close()
result = []
result_crf = []
result_rnn = []
key = 0
count = 0
for j in crf_a:
    if crf_c[key]!=rnn_pre[key]:
        count = count + 1
        result.append(crf_a[key])
        result_crf.append(crf_c[key])
        result_rnn.append(rnn_pre[key])
    
f1 = open('out.txt','w')
f2 = open('crf.txt','w')
f3 = open('rnn.txt','w')
print(result)
for i in result:
    f1.write(i)
    f1.write('\t')
f1.close()


for i in result_crf:
    f2.write(i)
    f2.write('\t')
f2.close()
         

for i in result_rnn:
    f3.write(i)
    f3.write('\t')
f3.close()

