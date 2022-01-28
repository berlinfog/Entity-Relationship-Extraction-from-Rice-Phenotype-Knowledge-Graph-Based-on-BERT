import sys, json
import torch
import os
import numpy as np
from multiprocessing import Pool
# sys.path.insert(0, '..')
# from opennre import encoder, model, 
from encoder.pcnn_encoder import PCNNEncoder
from softmax_nn import SoftmaxNN
from framework.sentence_re import SentenceRE

if __name__ == "__main__":
    p = Pool(4)
# Some basic settings
    root_path = '.'
    if not os.path.exists('ckpt'):
        os.mkdir('ckpt')
    ckpt = 'ckpt/rice_pcnn_0501-16-sgd.pth.tar'

    # Check data
    # opennre.download_nyt10(root_path=root_path)
    # opennre.download_glove(root_path=root_path)
    wordi2d = json.load(open('C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/pretrain/glove/test2.json','r',encoding='utf-8'))
    word2vec = np.load('C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/pretrain/glove/vec.npy')
    rel2id = json.load(open('C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/benchmark/rice-relation/data_rel2id.json','r',encoding='utf-8'))

    # Define the sentence encoder
    sentence_encoder = PCNNEncoder(
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

    # Define the model
    # model = BagAttention(sentence_encoder, len(rel2id), rel2id)
    model = SoftmaxNN(sentence_encoder, len(rel2id), rel2id)
    # Define the whole training framework
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
        opt='sgd')

    # Train the model
    framework.train_model()

    # Test the model
    framework.load_state_dict(torch.load(ckpt)['state_dict'])
    result = framework.eval_model(framework.test_loader)

    # Print the result
    f1=open("pcnn-16-sgd.txt","w",encoding="utf-8")
    print('AUC on test set: {}'.format(result['acc']))
    print('Micro Precision: {}'.format(result['micro_p']))
    print('Micro Recall: {}'.format(result['micro_r']))
    print('Micro F1: {}'.format(result['micro_f1']))
    
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
    f1.write(str(result))
    f1.write("\n")
    f1.write(str(s))