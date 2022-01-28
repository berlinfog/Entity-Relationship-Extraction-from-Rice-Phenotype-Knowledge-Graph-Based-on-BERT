import torch
import torch.utils.data as data
import os
import numpy as np
import random
import json
import sklearn.metrics

class SentenceREDataset(data.Dataset):
    """
    Sentence-level relation extraction dataset
    """
    def __init__(self, path, rel2id, tokenizer, kwargs):
        """
        Args:
            path: path of the input file
            rel2id: dictionary of relation->id mapping
            tokenizer: function of tokenizing
        """
        super().__init__()
        self.path = path
        self.tokenizer = tokenizer
        self.rel2id = rel2id
        self.kwargs = kwargs

        # Load the file
        f = open(path,encoding="utf-8")
        self.data = []
        for line in f.readlines():
            line = line.rstrip()
            if len(line) > 0:
                self.data.append(eval(line))
        f.close()
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, index):
        item = self.data[index]
        seq = list(self.tokenizer(item, **self.kwargs))
        res = [self.rel2id[item['relation']]] + seq
        return [self.rel2id[item['relation']]] + seq # label, seq1, seq2, ...
    
    def collate_fn(data):
        data = list(zip(*data))
        labels = data[0]
        seqs = data[1:]
        batch_labels = torch.tensor(labels).long() # (B)
        batch_seqs = []
        for seq in seqs:
            batch_seqs.append(torch.cat(seq, 0)) # (B, L)
        return [batch_labels] + batch_seqs
    
    def eval(self, pred_result, use_name=False):
        #计算正确率
        correct = 0
        total = len(self.data)
        correct_positive = 0
        pred_positive = 0
        gold_positive = 0
        neg = -1
        correctp0=0
        correctp1=0
        correctp2=0
        correctp3=0
        correctp4=0
        correctp5=0
        correctp6=0
        correctp7=0
        fp0=0
        fp1=0
        fp2=0
        fp3=0
        fp4=0
        fp5=0
        fp6=0
        fp7=0
        # num=0
        for name in ["NA", "na", "no_relation", "other", "Others"]:
            # print(self.rel2id)
            if name in self.rel2id:
                if use_name:
                    neg = name
                else:
                    neg = self.rel2id[name]
                break

        # print("neg",neg)5
        for i in range(total):
            if use_name:
                golden = self.data[i]['relation']
            else:
                golden = self.rel2id[self.data[i]['relation']]
            # if golden==4 :
            #     print("you")
            # if pred_result[i]==4 :
            #     print("you2")
            if golden == pred_result[i]:
                # print(golden)
                correct += 1
                ##############
                if golden==0:
                    correctp0+=1
                elif golden==1:
                    correctp1+=1
                elif golden==2:
                    correctp2+=1
                elif golden==3:
                    correctp3+=1
                elif golden==4:
                    correctp4+=1
                elif golden==5:
                    correctp5+=1
                elif golden==6:
                    correctp6+=1
                else:
                    correctp7+=1
                    # print("tp4")
                ###############
                if golden != neg:
                    correct_positive += 1
            if golden != neg:
                gold_positive +=1
            if pred_result[i] != neg:
                pred_positive += 1
            if golden != pred_result[i]:
                if pred_result[i]==0:
                    fp0+=1
                elif pred_result[i]==1:
                    fp1+=1
                elif pred_result[i]==2:
                    fp2+=1
                elif pred_result[i]==3:
                    fp3+=1
                elif pred_result[i]==4:
                    fp4+=1
                elif pred_result[i]==5:
                    fp5+=1
                elif pred_result[i]==6:
                    fp6+=1
                elif pred_result[i]==7:
                    fp7+=1
                    # print("fp4")
        # print("total=",total)      
        if float(fp0+correctp0)>0 and float(total-correct-fp0+correctp0)>0:
            precision0=float(correctp0)/float(fp0+correctp0)
            recall0=float(correctp0)/float(total-correct-fp0+correctp0)
            if float(precision0+recall0)>0:
                f10=2*precision0*recall0/(precision0+recall0)
            else:
                f10=0.1
        else:
            precision0=0
            recall0=0
            f10=0

        if float(fp1+correctp1)>0 and float(total-correct-fp1+correctp1)>0:
            precision1=float(correctp1)/float(fp1+correctp1)
            recall1=float(correctp1)/float(total-correct-fp1+correctp1)
            if float(precision1+recall1)>0:
                f11=2*precision1*recall1/(precision1+recall1)
            else:
                f11=0.1
        else:
            precision1=0
            recall1=0
            f11=0

        if float(fp2+correctp2)>0 and float(total-correct-fp2+correctp2)>0:
            precision2=float(correctp2)/float(fp2+correctp2)
            recall2=float(correctp2)/float(total-correct-fp2+correctp2)
            if float(precision2+recall2)>0:
                f12=2*precision2*recall2/(precision2+recall2)
            else:
                f12=0.1
        else:
            precision2=0
            recall2=0
            f12=0
        if float(fp3+correctp3)>0 and float(total-correct-fp3+correctp3)>0:    
            precision3=float(correctp3)/float(fp3+correctp3)
            recall3=float(correctp3)/float(total-correct-fp3+correctp3)
            if float(precision3+recall3)>0:
                f13=2*precision3*recall3/(precision3+recall3)
            else:
                f13=0.1
        else:
            precision3=0
            recall3=0
            f13=0

        if float(fp4+correctp4)>0 and float(total-correct-fp4+correctp4)>0:
            precision4=float(correctp4)/float(fp4+correctp4)
            recall4=float(correctp4)/float(total-correct-fp4+correctp4)
            if float(precision4+recall4)>0:
                f14=2*precision4*recall4/(precision4+recall4)
            else:
                f14=0.1
        else:
            precision4=0
            recall4=0
            f14=0
        

        if float(fp5+correctp5)>0 and float(total-correct-fp5+correctp5)>0:
            precision5=float(correctp5)/float(fp5+correctp5)
            recall5=float(correctp5)/float(total-correct-fp5+correctp5)
            if float(precision5+recall5)>0:
                f15=2*precision5*recall5/(precision5+recall5)
            else:
                f15=0.1
        else:
            precision5=0
            recall5=0
            f15=0
        
        if float(fp6+correctp6)>0 and float(total-correct-fp6+correctp6)>0:
            precision6=float(correctp6)/float(fp6+correctp6)
            recall6=float(correctp6)/float(total-correct-fp6+correctp6)
            if float(precision6+recall6)>0:
                f16=2*precision6*recall6/(precision6+recall6)
            else:
                f16=0.1
        else:
            precision6=0
            recall6=0
            f16=0
        
        if float(fp7+correctp7)>0 and float(total-correct-fp7+correctp7)>0:
            precision7=float(correctp7)/float(fp7+correctp7)
            recall7=float(correctp7)/float(total-correct-fp7+correctp7)
            if float(precision7+recall7)>0:
                f17=2*precision7*recall7/(precision7+recall7)
            else:
                f17=0.1
        else:
            precision7=0
            recall7=0
            f17=0
        
        acc = float(correct) / float(total)
        micro_p = float(correct_positive) / float(pred_positive)
        micro_r = float(correct_positive) / float(gold_positive)
        micro_f1 = 2 * micro_p * micro_r / (micro_p + micro_r)
        return {'acc': acc, 'micro_p': micro_p, 'micro_r': micro_r, 'micro_f1': micro_f1,'precision0':precision0,'recall0':recall0,'f10':f10,'precision1':precision1,'recall1':recall1,'f11':f11,'precision2':precision2,'recall2':recall2,'f12':f12,'precision3':precision3,'recall3':recall3,'f13':f13,'precision4':precision4,'recall4':recall4,'f14':f14,'precision5':precision5,'recall5':recall5,'f15':f15,'precision6':precision6,'recall6':recall6,'f16':f16,'precision7':precision7,'recall7':recall7,'f17':f17}
    
def SentenceRELoader(path, rel2id, tokenizer, batch_size, 
        shuffle, num_workers=8, collate_fn=SentenceREDataset.collate_fn, **kwargs):
    dataset = SentenceREDataset(path = path, rel2id = rel2id, tokenizer = tokenizer, kwargs=kwargs)
    data_loader = data.DataLoader(dataset=dataset,
            batch_size=batch_size,
            shuffle=shuffle,
            pin_memory=True,
            num_workers=num_workers,
            collate_fn=collate_fn)
    return data_loader