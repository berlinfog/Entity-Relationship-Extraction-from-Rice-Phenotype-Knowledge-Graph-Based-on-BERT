from encoder.bert_encoder import BERTEncoder
from encoder.cnn_encoder import CNNEncoder
from encoder.pcnn_encoder import PCNNEncoder
from softmax_nn import SoftmaxNN
import torch
import os
import sys
import json
import numpy as np


default_root_path = 'C:/Users/10750/Desktop/fourth/bishe/prosess_record/3BERT2/'
def get_model(model_name, root_path=default_root_path):
    ckpt = os.path.join(root_path, 'example/ckpt/' + model_name + '.pth.tar')
    if model_name == 'rice_bertbest':
        rel2id = json.load(open(os.path.join(root_path, 'benchmark/rice-relation/data_rel2id.json'),"r",encoding="utf-8"))
        sentence_encoder = BERTEncoder(
            max_length=80, pretrain_path=os.path.join(root_path, 'pretrain/chinese_wwm_pytorch'))
        m = SoftmaxNN(sentence_encoder, len(rel2id), rel2id)
        m.load_state_dict(torch.load(ckpt)['state_dict'])
        return m    

    else:
        raise NotImplementedError



model=get_model('rice_bertbest', root_path=default_root_path)
result = model.infer({'text': 'Pi-ta介导的稻瘟病抗性必须有Ptr(t)的参与', 'h': {'pos': (0, 4)}, 't': {'pos': (8, 12)}})
print(result)