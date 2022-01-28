# coding:utf-8
import torch
import numpy as np
import json
import os,sys
from multiprocessing import Pool
# from opennre import encoder, model, framework

from encoder.cnn_encoder import CNNEncoder
from framework.sentence_re import SentenceRE
from softmax_nn import SoftmaxNN

if __name__ == "__main__":
    p = Pool(4)
    ckpt = 'ckpt/semeval_cnn0501-16-sgd_softmax.pth.tar'
    wordi2d = json.load(open('C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/pretrain/glove/test2.json','r',encoding='utf-8'))
    word2vec = np.load('C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/pretrain/glove/vec.npy')
    rel2id = json.load(open('C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/benchmark/rice-relation/data_rel2id.json','r',encoding='utf-8'))
    sentence_encoder = CNNEncoder(
        token2id=wordi2d,
        max_length=100,
        word_size=100,
        position_size=5,
        hidden_size=230,
        blank_padding=True,
        kernel_size=3,
        padding_size=1,
        word2vec=None,
        dropout=0.5)
    model = SoftmaxNN(sentence_encoder, len(rel2id), rel2id)
    framework = SentenceRE(
        train_path='C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/benchmark/rice-relation/train0511.txt',
        val_path='C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/benchmark/rice-relation/test0511.txt',
        test_path='C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/benchmark/rice-relation/test0511.txt',
        model=model,
        ckpt=ckpt,
        batch_size=16,
        max_epoch=5,
        lr=0.1,
        weight_decay=1e-5,
        opt='adamw')
    # Train
    framework.train_model(metric='micro_f1')
    # Test
    framework.load_state_dict(torch.load(ckpt)['state_dict'])
    result = framework.eval_model(framework.test_loader)
    print('Accuracy on test set: {}'.format(result['acc']))
    print('Micro Precision: {}'.format(result['micro_p']))
    print('Micro Recall: {}'.format(result['micro_r']))
    print('Micro F1: {}'.format(result['micro_f1']))
    # print('all: {}'.format(result))
    s=[]
    s0='Precision0: '+str(result['precision0'])+' recall0: '+str(result['recall0'])+' f10: '+str(result['f10'])
    s.append(s0)
    s1='Precision1: '+str(result['precision1'])+' recall1:'+str(result['recall1'])+' f11: '+str(result['f11'])
    s.append(s1)
    s2='Precision2: '+str(result['precision2'])+' recall2: '+str(result['recall2'])+' f12: '+str(result['f12'])
    s.append(s2)
    s3='Precision3: '+str(result['precision3'])+' recall3: '+str(result['recall3'])+' f13: '+str(result['f13'])
    s.append(s3)
    s4='Precision4: '+str(result['precision4'])+' recall4: '+str(result['recall4'])+' f14: '+str(result['f14'])
    s.append(s4)

    for e in s:
        print(e)
        print("\n")
    f1=open("cnn-16-adamw.txt","w",encoding="utf-8")
    f1.write(str(result))
    f1.write("\n")
    f1.write(str(s))