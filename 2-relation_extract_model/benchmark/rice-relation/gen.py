# -*- coding:utf-8 -*-
# Copyright @rui.tao
import codecs
import sys
import pandas as pd
import numpy as np
from collections import deque
import pdb
import json

    
def get_pose(text, E_name):
    result = []
    pose_1 = text.find(E_name)
    pose_2 = pose_1+len(E_name)-1
    result.append(pose_1)
    result.append(pose_2)
    return result

f = open('train0511.txt', "w",encoding='utf-8') 
f2 = open('test0511.txt', "w",encoding='utf-8') 
people_relation = "train.txt"
people_relation2 = "test.txt"

with codecs.open(people_relation,'r',encoding='utf-8') as tfc:
    for lines in tfc:
        line = lines.split()
        data = {} 
        print(line)
        # if len(line)!=4:
        #     print(line)
        E1, E2, relation, text = line
        data["token"] = list(text)
        h = {}
        h["name"] = E1
        h["pos"] = get_pose(text, E1) 
        data["h"] = h
        t = {}
        t["name"] = E2
        t["pos"] = get_pose(text, E2)
        data["t"] = t
        data["relation"] = relation 
        json_data = json.dumps(data, ensure_ascii=False)
        f.write(json_data)
        f.write("\n")

        #print(json_data)
        #import sys
        #sys.exit()
with codecs.open(people_relation2,'r',encoding='utf-8') as tfc:
    for lines in tfc:
        line = lines.split()
        data = {} 
        print(line,len(line))
        # if len(line)>4:
        #     print(line)
        E1, E2, relation, text = line
        data["token"] = list(text)
        h = {}
        h["name"] = E1
        h["pos"] = get_pose(text, E1) 
        data["h"] = h
        t = {}
        t["name"] = E2
        t["pos"] = get_pose(text, E2)
        data["t"] = t
        data["relation"] = relation 
        json_data = json.dumps(data, ensure_ascii=False)
        f2.write(json_data)
        f2.write("\n")
        




