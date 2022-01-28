import os
def dele():
    allset=set()
    # handledoc = os.path.abspath(os.path.join(os.getcwd(),"./diff/"))
    handledoc = os.path.abspath(os.path.join(os.getcwd(),"./all/"))
    fw1=open('train.txt', 'w', encoding='utf-8')
    fw2=open('test.txt', 'w', encoding='utf-8')
    num=0
    num1=0
    for root,dirs,files in os.walk(handledoc):
        for file in files:
                num=0
                num1=0
                filePath = os.path.join(root,file)
                print(filePath)
                with open(filePath,'r',encoding='utf-8',errors='ignore') as fr:
                    for e in fr:
                        num+=1
                    print(num)
                    frr=open(filePath,'r',encoding='utf-8',errors='ignore')
                    for e in frr:
                        if num1<num*0.8 and e:
                            num1+=1
                            s=e.replace(" ","")
                            if e!="\n":
                                fw1.write(s.replace(" ",""))
                        elif num1>=num*0.8 and e:
                            num1+=1
                            s=e.replace(" ","")
                            if e!="\n":
                                fw2.write(s.replace(" ",""))
                        else:
                            num1+=1
                            continue
                    print(num1)
                fw2.write("\n")
    # allset=set()
    # fre = open('data_frequency.txt', 'w', encoding='utf-8')
    # i={'instance of':0,'taxon rank':0,'subclass of':0,'has part':0,'parent taxon':0,'part of':0,'different from':0,'has fruit type':0,'found in taxon':0,'color':0}
    # # print(str(os.getcwd()))
    # handledoc = os.path.abspath(os.path.join(os.getcwd(),"./handledoc/"))
    # dic1=['instance of','taxon rank','subclass of','has part','parent taxon','part of','different from','has fruit type','found in taxon','color']
    # fw1=open("0501subclass.txt",'w',encoding="utf8",errors="ignore")
    # fw2=open("0501diff.txt",'w',encoding="utf8",errors="ignore")
    # fw3=open("0501color.txt",'w+',encoding="utf8",errors="ignore")
    # with open("datahandled.txt",'w+',encoding="utf8",errors="ignore") as fw:
    #     for root,dirs,files in os.walk(handledoc):
    #         for file in files:
    #             filePath = os.path.join(root,file)
    #             print(filePath)
    #             with open(filePath,'r',encoding='utf-8',errors='ignore') as fr:
    #                 for e in fr:
    #                     # print(e)
    #                     fk=e.split()
    #                     if len(fk)<2:
    #                         continue
    #                     fk[2]=fk[2].replace(" ","_")
    #                     ek=fk[0]+fk[1]+fk[2]+fk[3]
    #                     if ek not in allset:
    #                         allset.add(ek)
    #                         for kkk in dic1:
    #                             if kkk in e and fk[0] in fk[-1] and fk[1] in fk[-1]:
    #                                 i[kkk]+=1
    #                                 fw.write(fk[0]+"\t"+fk[1]+"\t"+kkk.replace(" ","_")+"\t"+fk[-1].replace(" ","")+"\n")
    #                                 if kkk=='subclass of':
    #                                     fw1.write(fk[0]+"\t"+fk[1]+"\t"+kkk.replace(" ","_")+"\t"+fk[-1].replace(" ","")+"\n")
    #                                 elif kkk=='different from':
    #                                     fw2.write(fk[0]+"\t"+fk[1]+"\t"+kkk.replace(" ","_")+"\t"+fk[-1].replace(" ","")+"\n")
    #                                 elif kkk=='color':
    #                                     fw3.write(fk[0]+"\t"+fk[1]+"\t"+kkk.replace(" ","_")+"\t"+fk[-1].replace(" ","")+"\n")
    #                                 else:
    #                                     continue
    #                             if kkk.replace(" ","_") in e and fk[0] in fk[-1] and fk[1] in fk[-1]:
    #                                 i[kkk]+=1
    #                                 fw.write(fk[0]+"\t"+fk[1]+"\t"+kkk.replace(" ","_")+"\t"+fk[-1].replace(" ","")+"\n")
    #                                 if kkk=='subclass of':
    #                                     fw1.write(fk[0]+"\t"+fk[1]+"\t"+kkk.replace(" ","_")+"\t"+fk[-1].replace(" ","")+"\n")
    #                                 elif kkk=='different from':
    #                                     fw2.write(fk[0]+"\t"+fk[1]+"\t"+kkk.replace(" ","_")+"\t"+fk[-1].replace(" ","")+"\n")
    #                                 elif kkk=='color':
    #                                     fw3.write(fk[0]+"\t"+fk[1]+"\t"+kkk.replace(" ","_")+"\t"+fk[-1].replace(" ","")+"\n")
    #                                 else:
    #                                     continue

                        
    # fre.write(str(i))
    # num=0
    # for key,value in i.items():
    #     num+=value
    # print(num)
    
dele()