import os
import csv
def dele():
    aaa=[]
    ddd=[]
    headers = ['title','lable']
    headers2=['HudongItem1','relation','HudongItem2']
    # handledoc = os.path.abspath(os.path.join(os.getcwd(),"./diff/"))
    handledoc = os.path.abspath(os.path.join(os.getcwd(),"./all/"))
    fw1=open('new_node.csv', 'w',newline='', encoding='utf-8')
    fw2=open('rice_relation.csv', 'w',newline='', encoding='utf-8')
    for root,dirs,files in os.walk(handledoc):
        for file in files:
                filePath = os.path.join(root,file)
                print(filePath)
                with open(filePath,'r',encoding='utf-8',errors='ignore') as fr:
                    for e in fr:
                        if e!="\n":
                            fk=e.split()
                            # print(e)
                            bbb=[str(fk[0]),'newNode']
                            aaa.append(bbb)
                            bbb=[str(fk[1]),'newNode']
                            aaa.append(bbb)
                            ccc=[str(fk[0]),str(fk[2]),str(fk[1])]
                            ddd.append(ccc)
    list_a = list()
    for i in aaa:
        if i not in list_a:
            list_a.append(i)
    list_d = list()
    for i in ddd:
        if i not in list_d:
            list_d.append(i)
    f_csv = csv.writer(fw1)
    f_csv.writerow(headers)
    f_csv.writerows(list_a)

    f_csv = csv.writer(fw2)
    f_csv.writerow(headers2)
    f_csv.writerows(list_d)

            
    
dele()