# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 19:09:23 2018

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


file_path='e:\\CCKS2017\\ccks2_test_dataset\\test dataset\\02-病史特点-format2\\'
file_name = '病史特点-301.txtoriginal.txt'
#files = os.listdir(file_path)
#for x in files:

f= open(os.path.join(file_path,file_name),'r',encoding='UTF-8')
bstd_b = f.read()
#result = np.zeros([len(bstd_b),2],dtype = np.string_)
#result.tolist()
f_temp = open('d:\\test.txt','w')
        
for i in bstd_b:
    f_temp.write(i)
    f_temp.write('\n')
    #result[m_key][0] = bstd_b[m_key].decode('ascii', 'ignore').encode('utf-8')
f_temp.close()
f_temp = open('d:\\test.txt','r')
result = f_temp.read()
result = np.array(result.split('\n'))
temp_n = 0
for n in result:
    if n=='':
        temp_n = temp_n + 1
result = result[:-temp_n]
result = result.reshape([len(result),1])
feature = ""
#huanhang = ""
for i in result:
    feature = feature + 'N'
    #huanhang = huanhang + '\n'
feature = list(feature)

feature = np.array(feature)
feature = feature.reshape([len(feature),1])
out = np.append(result,feature,axis=1)

out_f = open('E:\\zh-NER-TF-master\\zh-NER-TF-master\\test.txt','w',encoding='utf-8')
for i in out:
    for j in i:
        if j == '。':
            out_f.write('\n')
            break
        else:
            out_f.write(j)
            out_f.write('\t')
    out_f.write('\n')
out_f.close()
