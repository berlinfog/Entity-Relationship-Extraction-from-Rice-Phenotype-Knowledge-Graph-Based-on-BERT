# -*- coding: utf-8 -*-

import os
import thulac
import sys
import re
sys.path.append("..")
from toolkit.pre_load import pre_load_thu,neo_con,predict_labels
from toolkit.NER import get_NE,temporaryok,get_explain,get_detail_explain
import json
numm=0
set0=set()
stopToken = "。！？"
def getyin(s):
	k=""
	flag=-1
	for i in s:
		if ord(i)==39:
			flag=flag*(-1)
		elif ord(i)!=39 and flag==1:
			k+=i
		else:
			continue
	return k


def CutStatements(line):
	statements = []
	tokens = []
	for token in line:
		tokens.append(token)
		#如果是句子停止词
		if(token in stopToken):			
			statements.append(''.join(tokens))
			tokens = []
	if( len(tokens)>2 ):
		statements.append(''.join(tokens)+"。")
	return statements

punctuation = '!、“”()（）:，。,;:?"\''
def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation),'',text)
    return text.strip()

thu = pre_load_thu #预先加载好
#连接数据库
db = neo_con

corpusPath = os.path.abspath(os.path.join(os.getcwd(),"../wikiextractor/extracted/2/"))
#获取已经处理过得文件
fileReadedList = []
with open("fileReaded.txt","r",encoding="utf8",errors="ignore") as fileReaded:
	for line in fileReaded:
		fileReadedList.append(line.strip())
		# print(line.strip())
#递归遍历语料库文件夹
with open('train_data_0501.txt',"w",encoding="utf8",errors="ignore") as fw:
	with open("fileReaded.txt","a") as filereaded:
		fw.write('caonima')
		fw.flush()
		for root,dirs,files in os.walk(corpusPath):			
			for file in files:
				filePath = os.path.join(root,file)
				if(filePath in fileReadedList):
					continue
				if(len(file) > 7 and file[-7:] == 'zh_hans' ):
					with open(filePath,'r',encoding='utf-8',errors='ignore') as fr:
					
						count = 0
						for line in fr:
							count += 1
							# if(count%100 == 0):
							# 	print(filePath+"  "+str(count))
							#过滤掉<doc >  </doc> 等无用行
							if(len(line)< 2 or line[0:4] == '<doc' or line[0:6] == "</doc>"):
								continue
							#分句
							statements = CutStatements(line)
							for statement1 in statements:
								#分词
								# print(statement)
								statement=removePunctuation(statement1).replace("/'","")
								cutResult = get_NE(statement.strip())
								#得到每句话的实体列表后，两两匹配查询是否具有某种关系,如果有的话就写到文件中
								#entityList 存储实体列表和实体出现的位置,entity1存储实体名称，entity1Index存储实体位置
								entityList = []
								nowIndex = -1
								for word in cutResult:
									if(word[1]!=0 and not temporaryok(word[1])):
										entity1Index = statement.index(word[0],nowIndex+1)
										entityList.append({'entity1':removePunctuation(word[0]).replace("'",""),'entity1Index':entity1Index})
										nowIndex = entity1Index+len(word[0])-1

								entityNumber = len(entityList)
								# print(entityList)
								for i in range(entityNumber):
									answer = None
									#answer = entityRelationDict.get(entityList[i].get('entity1'))
									#if(entityRelationDict.get(entityList[i].get('entity1')) is None):
									answer = db.findRelationByEntity2(entityList[i].get('entity1'))
										#entityRelationDict[entityList[i].get('entity1')] = answer
									for relation in answer:
										#对neo4j的返回值进行处理，原来的返回值中包含一些没用的字符，最终得到的关系是rel,实体是entity2
										relation1=str(relation['n1']).encode().decode('unicode_escape')
										# print(relation1)
										if relation1.find("detail:")==-1:
											continue
										
										n1=relation1[relation1.index("title:")+8:relation1.index("url:")-3]
										# print("title"+n1)
										rel = str(getyin(str(relation['rel']))).encode().decode('unicode_escape')
										if rel=='instance of' or rel=='taxon rank' or rel=='subclass of' or rel=='has part' or rel=='parent taxon' or rel=='part of' or rel=='different from' or rel=='has fruit type' or rel=='found in taxon' or rel=='color': 
											pass
										else:
											continue
										# print("rel"+rel)
										# print(entityList[i].get('entity1'))
										# print("文字"+statement+"n1"+n1+"n2"+entityList[i].get('entity1'))

										if statement.find(n1)!=-1 and statement.find(entityList[i].get('entity1'))!=-1 and entityList[i].get('entity1').find(n1)==-1 and  n1.find(entityList[i].get('entity1'))==-1 and entityList[i].get('entity1')!=n1 and statement.find(n1)<60 and statement.find(entityList[i].get('entity1'))<60:
											# set0.add(entityList[i].get('entity1')+" "+n1+" "+rel+" "+statement+"\n")
											k=entityList[i].get('entity1').replace(" ","")+"\t"+n1.replace(" ","")+"\t"+rel.replace(" ","_")+"\t"+statement.replace(" ","")+"\n"
											if k not in set0:
												numm+=1
												# print("计数："+str(numm)+"\n")
												set0.add(k)
												fw.write(k)
												fw.flush()
												# print(k)
											else:
												continue

					filereaded.write(filePath+'\n')
									
fw.close()			
				


