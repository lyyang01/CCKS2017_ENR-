# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 14:08:21 2018

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

file_path='e:\\CCKS2017\\CCKS2017_dataset\\case_of_illness\\data2\\training dataset v4\\病史特点\\'
files = os.listdir(file_path)
user_dict = {}

for x in files:
    s = re.match('病史特点-(\d+).txt\Z',x)  ##从字符串末尾开始匹配
    if s:
        #print(x)
        f = open(os.path.join(file_path, x),'r',encoding='UTF-8')
        bstd = f.read()
        #print(bstd)
        temp = re.split('[\t\n]', bstd)  ##re可以使用多个分隔符
        temp = temp[:-1]
        temp = np.array(temp)
        temp = temp.reshape((-1,4))
        print(temp)
        for i in temp:
            try:
                user_dict[i[0]] = user_dict[i[0]] + 1
            except:
                user_dict[i[0]]=1



key = list(user_dict.keys())
temp = len(key)
key = np.array(key).reshape([temp,1])
value = list(user_dict.values())
temp = len(value)
value = np.array(value).reshape([temp,1])

out = np.append(key,value,axis = 1)

out_f = open('usr_dict_bstd.txt','w',encoding='utf-8')
for i in out:
    for j in i:
        out_f.write(j)
        out_f.write(' ')
    out_f.write('\n')
out_f.close()      
        
#print(user_dict)
                
                
                
                
                
                