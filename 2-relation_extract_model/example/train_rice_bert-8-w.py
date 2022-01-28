import sys, json
import torch
import os
import numpy as np
from framework.sentence_re import SentenceRE
from softmax_nn import SoftmaxNN
from encoder.bert_encoder import BERTEncoder

import argparse
from multiprocessing import Pool

#修改24 38-40
if __name__ == "__main__":
    p = Pool(4)
    parser = argparse.ArgumentParser()
    parser.add_argument('--mask_entity', action='store_true', help='Mask entity mentions')
    args = parser.parse_args()  

    # Some basic settings
    root_path = 'C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/'
    sys.path.append(root_path)
    if not os.path.exists('ckpt'):
        os.mkdir('ckpt')
    ckpt = 'ckpt/rice_bert_8_w_softmax.pth.tar'   

    # Check data
    rel2id = json.load(open('C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/benchmark/rice-relation/data_rel2id.json','r',encoding='utf-8'))   

    # Define the sentence encoder
    sentence_encoder = BERTEncoder(
        max_length=80, 
        pretrain_path=os.path.join(root_path, 'pretrain/chinese_wwm_pytorch/'),
        mask_entity=args.mask_entity
    )   

    # Define the model
    model = SoftmaxNN(sentence_encoder, len(rel2id), rel2id)  

    # Define the whole training framework
    framework =SentenceRE(
        train_path=os.path.join(root_path, 'benchmark/rice-relation/train0511.txt'),
        val_path=os.path.join(root_path, 'benchmark/rice-relation/test0511.txt'),
        test_path=os.path.join(root_path, 'benchmark/rice-relation/test0511.txt'),
        model=model,
        ckpt=ckpt,
        batch_size=8, # Modify the batch size w.r.t. your device
        max_epoch=5,
        lr=2e-5,
        opt='adamw'
    )   

    # Train the model
    framework.train_model() 

    # Test the model
    framework.load_state_dict(torch.load(ckpt)['state_dict'])
    result = framework.eval_model(framework.test_loader)    

    # Print the result
    print('Accuracy on test set: {}'.format(result['acc']))
    print('Micro Precision: {}'.format(result['micro_p']))
    print('Micro Recall: {}'.format(result['micro_r']))
    print('Micro F1: {}'.format(result['micro_f1']))
    s=[]
    s0='Precision0: '+str(result['precision0'])+' recall0: '+str(result['recall0'])+' f10: '+str(result['f10'])+"\n"
    s.append(s0)
    s1='Precision1: '+str(result['precision1'])+' recall1:'+str(result['recall1'])+' f11: '+str(result['f11'])+"\n"
    s.append(s1)
    s2='Precision2: '+str(result['precision2'])+' recall2: '+str(result['recall2'])+' f12: '+str(result['f12'])+"\n"
    s.append(s2)
    s3='Precision3: '+str(result['precision3'])+' recall3: '+str(result['recall3'])+' f13: '+str(result['f13'])+"\n"
    s.append(s3)
    s4='Precision4: '+str(result['precision4'])+' recall4: '+str(result['recall4'])+' f14: '+str(result['f14'])+"\n"
    s.append(s4)

    print(s)
    f1=open("bert-8-w.txt","w",encoding="utf-8")
    f1.write(str(result))
