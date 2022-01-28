from myweb0415.encoder.bert_encoder import BERTEncoder
from  myweb0415.encoder.cnn_encoder import CNNEncoder
from  myweb0415.encoder.pcnn_encoder import PCNNEncoder
from  myweb0415.softmax_nn import SoftmaxNN
# from . import model
# from . import framework
import torch
import os
import sys
import json
import numpy as np


default_root_path = 'C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/'
def get_model(model_name, root_path=default_root_path):
    ckpt = os.path.join(root_path, 'example/ckpt/' + model_name + '.pth.tar')
    if model_name == 'rice_bertbest':
        print("got it")
        rel2id = json.load(open(os.path.join(root_path, 'benchmark/rice-relation/data_rel2id.json'),"r",encoding="utf-8"))
        sentence_encoder = BERTEncoder(
            max_length=80, pretrain_path=os.path.join(root_path, 'pretrain/chinese_wwm_pytorch'))
        m = SoftmaxNN(sentence_encoder, len(rel2id), rel2id)
        m.load_state_dict(torch.load(ckpt)['state_dict'],False)
        return m    
    elif model_name == 'rice_bert_softmax':
        rel2id = json.load(open(os.path.join(root_path, 'benchmark/rice-relation/data_rel2id.json'),"r",encoding="utf-8"))
        sentence_encoder = BERTEncoder(
            max_length=80, pretrain_path=os.path.join(root_path, 'pretrain/chinese_wwm_pytorch'))
        m = SoftmaxNN(sentence_encoder, len(rel2id), rel2id)
        m.load_state_dict(torch.load(ckpt)['state_dict'])
        return m    

    elif model_name == 'rice_cnn_softmax':
        wordi2d = json.load(open(os.path.join(root_path,'pretrain/glove/test2.json'),'r',encoding='utf-8'))
        word2vec = np.load(os.path.join(root_path,'pretrain/glove/vec.npy'))
        rel2id = json.load(open(os.path.join(root_path,'benchmark/rice-relation/data_rel2id.json'),'r',encoding='utf-8'))
        sentence_encoder = CNNEncoder(token2id=wordi2d,
                                                    max_length=100,
                                                    word_size=100,
                                                    position_size=5,
                                                    hidden_size=230,
                                                    blank_padding=True,
                                                    kernel_size=3,
                                                    padding_size=1,
                                                    word2vec=word2vec,
                                                    dropout=0.5)
        m = SoftmaxNN(sentence_encoder, len(rel2id), rel2id)
        m.load_state_dict(torch.load(ckpt)['state_dict'])
        return m
    
    elif model_name == 'rice_pcnn_softmax':
        wordi2d = json.load(open('C:/Users/10750/Desktop/fourth/bishe/BERT/github/OpenNRE-master/pretrain/glove/test2.json','r',encoding='utf-8'))
        word2vec = np.load('C:/Users/10750/Desktop/fourth/bishe/BERT/github/OpenNRE-master/pretrain/glove/vec.npy')
        rel2id = json.load(open('C:/Users/10750/Desktop/fourth/bishe/BERT/github/OpenNRE-master/benchmark/rice-relation/data_rel2id.json','r',encoding='utf-8'))
        sentence_encoder = sentence_encoder = PCNNEncoder(
            token2id=wordi2d,
            max_length=120,
            word_size=100,
            position_size=5,
            hidden_size=230,
            blank_padding=True,
            kernel_size=3,
            padding_size=1,
            word2vec=word2vec,
            dropout=0.5
        )
        m = SoftmaxNN(sentence_encoder, len(rel2id), rel2id)
        m.load_state_dict(torch.load(ckpt)['state_dict'])
        return m
    
    else:
        raise NotImplementedError



# model=get_model('rice_bert_softmax', root_path=default_root_path)
# result = model.infer({'text': '中国和印度在洞朗地区存在领土争端', 'h': {'pos': (0, 1)}, 't': {'pos': (3, 4)}})
# print(result)