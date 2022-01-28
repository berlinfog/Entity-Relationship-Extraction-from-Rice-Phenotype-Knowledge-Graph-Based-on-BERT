def fenlei():
	file_object = open('data_test.txt','r',encoding='utf-8').read().split('\n')
	x=set()
	kuang=[]
	dic1=dict()
	for f in file_object:
		fk=f.split()
		if len(fk)==4:
			# print(str(fk[2]))
			x.add(str(fk[2]))
		else:
			# print(str(fk[2:-2]))
			x.add(str(fk[2:-2]))
	i=[0]*len(x)
	print(x)
	x2=list(x)
	for f in file_object:
		fk=f.split()
		# print(fk)
		for e in range(len(x2)):
			if x2[e]==str(fk[2]):
				i[e]+=1
	print(i)
	# for e in range(len(x)):
	# 	dic1[str(x2[e])]=i[e]
	# data_list = sorted(zip(dic1.values(), dic1.keys()))
	# for e in data_list:
	# 	file_object2.write(str(e)+"\n")


	
fenlei()