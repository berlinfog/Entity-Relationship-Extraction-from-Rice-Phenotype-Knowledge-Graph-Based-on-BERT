import numpy as np
import json
import os
import collections
fw1=open("vec.txt","r",encoding="utf-8")
path = "test1.json"
num=0
word=[]
dic1=collections.OrderedDict()
list1=[]
list2=[]
for e in fw1:
    fk=e.split()
    # print(fk[0])
    word.append(fk[0])
    list1=[float(m) for m in fk[1:]]
    list2.append(list1)
    
arr=np.array(list2,dtype=np.float32)
print(type(arr))
print(arr.shape)
print(arr)
np.save('vec.npy', arr)
for e in word:
    dic1[e]=num
    num+=1

#先将字典对象转化为可写入文本的字符串
item = json.dumps(dic1, ensure_ascii=False)
try:
    with open(path, "w", encoding="utf-8") as f:
        f.write(item + ",\n")
        print("write success")
except Exception as e:
    print("write error==>", e)