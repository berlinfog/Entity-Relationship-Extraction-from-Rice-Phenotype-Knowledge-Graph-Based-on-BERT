import numpy as np
import json
import os
import collections
import codecs
import sys
import pandas as pd
import numpy as np
from collections import deque
import pdb
import json
import uuid

def get_pose(text, E_name):
    result = []
    pose_1 = text.find(E_name)
    pose_2 = pose_1+len(E_name)-1
    result.append(pose_1)
    result.append(pose_2)
    return result


f = open('data_test_after_pcnn.txt', "w+",encoding='utf-8') 

# 原始数据,数据来源：https://github.com/buppt/ChineseNRE
rice_relation = "data_test.txt"

with codecs.open(rice_relation,'r',encoding='utf-8') as tfc:
    for lines in tfc:
        line = lines.split()
        data = {} 
        # print(line,len(line))
        # if len(line)>4:
        #     print(line)
        E1, E2, relation, text = line
        data["text"] = str(line[3])
        data["relation"] = relation 
        h = {}
        namespace = uuid.NAMESPACE_URL
        h["id"]=str(uuid.uuid3(namespace,E1))
        h["name"] = E1
        h["pos"] = get_pose(text, E1) 
        data["h"] = h
        t = {}
        t["id"]=str(uuid.uuid3(namespace,E2))
        t["name"] = E2
        t["pos"] = get_pose(text, E2)
        data["t"] = t
        
        json_data = json.dumps(data,ensure_ascii=False)
        f.write(json_data+"\n")
        # f.write("\n")

# path = "test1.json"
# num=0
# word=[]
# dic1=collections.OrderedDict()
# list1=[]
# list2=[]
# for e in fw1:
#     fk=e.split()
#     # print(fk[0])
#     word.append(fk[0])
#     list1=[float(m) for m in fk[1:]]
#     list2.append(list1)
    
# arr=np.array(list2,dtype=np.float32)
# print(type(arr))
# print(arr.shape)
# print(arr)
# np.save('vec.npy', arr)
# for e in word:
#     dic1[e]=num
#     num+=1

# #先将字典对象转化为可写入文本的字符串
# item = json.dumps(dic1, ensure_ascii=False)
# try:
#     if not os.path.exists(path):
#         with open(path, "w", encoding="utf-8") as f:
#             f.write(item + ",\n")
#             print("^_^ write success")
#     else:
#         with open(path, "a", encoding="utf-8") as f:
#             f.write(item + ",\n")
#             print("^_^ write success")
# except Exception as e:
#     print("write error==>", e)