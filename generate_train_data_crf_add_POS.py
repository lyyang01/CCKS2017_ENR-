# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:42:24 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 21:23:46 2018

@author: Administrator
"""
import os
import os.path
import re
import numpy as np
import sys
import importlib
importlib.reload(sys)
import jieba
import jieba.posseg as psg


PYTHONIOENCODING='utf-8'


file_path='e:\\CCKS2017\\CCKS2017_dataset\\case_of_illness\\data2\\training dataset v4\\病史特点\\'
files = os.listdir(file_path)
my_dict = {'身体部位':'bodyloc','症状和体征':'ZZ','疾病和诊断':'ZD','检查和检验':'JC','治疗':'ZL'}  ##python中的字典
key = 1
for x in files:
    key = key + 1
    s = re.match('病史特点-(\d+).txtoriginal.txt',x)  ##从字符串末尾开始匹配
    if not s:
         f = open(os.path.join(file_path, x),'r',encoding='UTF-8')
         bstd_o = f.read()
         temp = re.split('[\t\n]', bstd_o)  ##re可以使用多个分隔符
         temp = temp[:-1]
         temp = np.array(temp)
         temp = temp.reshape((-1,4))
         print(x)
         #a = bstd_o.split('\t')
         #print(len(temp[0]))
           
    else:
        file_name = s.group()
        f= open(os.path.join(file_path,file_name),'r',encoding='UTF-8')
        bstd_b = f.read()
#TODO add fenci
        oo = []
        pp = [(x.word, x.flag) for x in psg.cut(bstd_b)]
        for i in pp:
            if i[0]!='\n' and i[0]!='\ufeff':
                for j in i[0]:       
                    if j!='.':
                        oo.append(i[1])
                    else:
                        oo.append('x')
        oo = np.array(oo)
        oo = oo.reshape([len(oo),1])
        print(len(oo))
        #result = np.zeros([len(bstd_b),2],dtype = np.string_)
        #result.tolist()
        f_temp = open('d:\\temp.txt','w')
        
        for i in bstd_b:
            if i!='\ufeff':
                #if i!=' ':
                f_temp.write(i)
                f_temp.write('\n')
            #result[m_key][0] = bstd_b[m_key].decode('ascii', 'ignore').encode('utf-8')
        f_temp.close()
        f_temp = open('d:\\temp.txt','r')
        result = f_temp.read()
        ##
        result = result.split('\n')
        result = [n for n in result if n != '']  ##可以删除list中的所有空元素

        result = np.array(result)
        temp_n = 0
        #for n in result:
        #    if n=='':
        #        temp_n = temp_n + 1
        #result = result[:-temp_n]
        result = result.reshape([len(result),1])
        feature = ""
        #huanhang = ""
        for i in result:
            feature = feature + 'N'
            #huanhang = huanhang + '\n'
        feature = list(feature)
        #huanhang = np.array(list(huanhang)).reshape([len(huanhang),1])

        for i in temp:
            if int(i[1]) == int(i[2]):
                feature[int(i[1])] = "S_"+ my_dict[i[3]]
            else:
                feature[int(i[1])] = "B_"+ my_dict[i[3]]
                feature[int(i[2])] = "E_"+ my_dict[i[3]]
                #print('\n')
                #print(i)
                for j in range(int(i[1])+1,int(i[2])):
                    feature[j] = "I_" + my_dict[i[3]]
        
        feature = np.array(feature)
        feature = feature.reshape([len(feature),1])
        print(len(feature))
        out = np.append(result,oo, axis=1)
        out = np.append(out, feature, axis=1)
       
        #out = np.append(np.append(result,feature,axis=1),huanhang,axis=1)
        #out = list(out.reshape([len(out)*3,]))
        #out = np.append(out,huanhang,axis=1)
        #out = list(out)
        #row = 0
        #for nn in out:
        #    if nn[0]==' ':
        #        out = np.delete(out,row,axis=0)
        #    row = row + 1
        
        #print(len(out))
        out_f = open('E:\\CCKS2017\\CRF++-0.58\\CRF++-0.58\\example\\my_train_ccks2017\\train_my_data.txt','a+',encoding='utf-8')
        for i in out:
            my_key = 0
            my_key1 = 0
            for j in i:
                if j == '。':
                    out_f.write(j)
                    out_f.write('\t')
                    my_key = my_key + 1
                elif j==' ':
                    my_key1 = my_key1 + 1
                    break
                else:
                    out_f.write(j)
                    out_f.write('\t')
            if my_key ==1:
                out_f.write('\n')
                out_f.write('\n')
            elif my_key1==0:
                out_f.write('\n')
        out_f.close()
        
        #if key > 8:
        #    break
  