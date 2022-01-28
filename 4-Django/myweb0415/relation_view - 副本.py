# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from toolkit.pre_load import neo_con
from django.http import JsonResponse
from .pretrainnew import get_model
import os

import json
relationCountDict = {}
filePath = os.path.abspath(os.path.join(os.getcwd(),"."))
with open(filePath+"/toolkit/relationStaticResult.txt","r",encoding='utf8') as fr:
	for line in fr:
		relationNameCount = line.split(",")
		relationName = relationNameCount[0][2:-1]
		relationCount = relationNameCount[1][1:-2]
		relationCountDict[relationName] = int(relationCount)
def sortDict(relationDict):
	for i in range( len(relationDict) ):
		relationName = relationDict[i]['rel']['type']
		relationCount = relationCountDict.get(relationName)
		if(relationCount is None ):
			relationCount = 0
		relationDict[i]['relationCount'] = relationCount

	relationDict = sorted(relationDict,key = lambda item:item['relationCount'],reverse = True)

	return relationDict
def relation_extract():
	sent="西藏是中国最大的一个省份，包括了阿里地区这个中国最大的地级市"
	en1="西藏"
	en2="阿里"
	model=get_model('rice_bert_softmax', root_path='C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/')
	result = model.infer({'text': '中国和印度在洞朗地区存在领土争端', 'h': {'pos': (0, 1)}, 't': {'pos': (3, 4)}})
	print(result)
	
def search_entity(request):
	ctx = {}
	#根据传入的实体名称搜索出关系
	if(request.GET):
		entity = request.GET['user_text']
		#连接数据库
		db = neo_con
		entityRelation = db.getEntityRelationbyEntity(entity)
		if len(entityRelation) == 0:
			#若数据库中无法找到该实体，则返回数据库中无该实体
			ctx= {'title' : '<h1>数据库中暂未添加该实体</h1>'}
			return render(request,'entity.html',{'ctx':json.dumps(ctx,ensure_ascii=False)})
		else:
			#返回查询结果
			#将查询结果按照"关系出现次数"的统计结果进行排序
			entityRelation = sortDict(entityRelation)

			return render(request,'entity.html',{'entityRelation':json.dumps(entityRelation,ensure_ascii=False)})

	return render(request,"entity.html",{'ctx':ctx})
relation_extract()