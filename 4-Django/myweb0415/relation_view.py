# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from weblrl import models
from toolkit.pre_load import neo_con
import myweb0415.pretrainnew
import os
import paramiko
import json
#59行
relationCountDict = {}
filePath = os.path.abspath(os.path.join(os.getcwd(),"."))
def relation_extract(request):
	# sent="西藏是中国最大的一个省份，包括了阿里地区这个中国最大的地级市"
	# en1="西藏"
	# en2="阿里"
	result=()
	if request.method=='POST':
		sentence=request.POST.get("sentence",None)
		entity1 = request.POST.get("entity1", None)
		entity2 = request.POST.get("entity2", None)
		e1=(sentence.find(entity1),sentence.find(entity1)+len(entity1)-1)
		e2=(sentence.find(entity2),sentence.find(entity2)+len(entity2)-1)
		model=myweb0415.pretrainnew.get_model('rice_bertbest', root_path='C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/')
		result = model.infer({'text': sentence, 'h': {'pos': e1}, 't': {'pos': e2}})
		# print(request.session['user_name'])
		if request.session.has_key('user_name'):
			new_rela = models.relation.objects.create()
			new_rela.name = request.session['user_name']
			new_rela.sentence = sentence
			new_rela.entity1 = entity1
			new_rela.entity2 = entity2
			new_rela.result = result[0]
			new_rela.save()
		return render(request,"relation_extract.html",{"result":result[0]})
	return render(request,"relation_extract.html",{"result":''})

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
			s=''
			for e in entityRelation:
				s+=str(e['entity2']['title'])
				s+=" "
			if request.session.has_key('user_name'):
				# models.entity.objects.filter(name=request.session['user_name']).delete()
				new_entity = models.entity.objects.create()
				new_entity.name = request.session['user_name']
				new_entity.entity = entity
				new_entity.friend=s
				new_entity.save()
			# print(entity,type(entity))
			return render(request,'entity.html',{'entityRelation':json.dumps(entityRelation,ensure_ascii=False)})

	return render(request,"entity.html",{'ctx':ctx})


def ask(request):
	# sent="西藏是中国最大的一个省份，包括了阿里地区这个中国最大的地级市"
	# en1="西藏"
	# en2="阿里"
	if(request.GET):
		ask = request.GET['user_text']
		client = paramiko.SSHClient()
		# 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(hostname='39.100.233.32', port=22, username='root', password='L12r18l12,')
		stdin, stdout, stderr = client.exec_command('curl 127.0.0.1:8999/anyq?question='+str(ask))
		# print(request.session['user_name'])
		answer1=stdout.read().decode('utf-8')
		answer2=answer1[answer1.find("answer")+9:answer1.find("confidence")-3]
		answer3=answer2.encode('utf-8').decode('unicode_escape')
		if request.session.has_key('user_name'):
			new_rela = models.question.objects.create()
			new_rela.name = request.session['user_name']
			new_rela.question = ask
			new_rela.answer=answer3
			new_rela.save()
		return render(request,"ask.html",{"result":answer3})
	return render(request,"ask.html",{"result":''})