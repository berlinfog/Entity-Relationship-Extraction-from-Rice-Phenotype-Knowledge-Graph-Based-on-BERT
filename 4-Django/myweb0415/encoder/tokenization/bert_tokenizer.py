

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import unicodedata
import six

from .basic_tokenizer import BasicTokenizer
from .word_piece_tokenizer import WordpieceTokenizer
from .utils import (convert_to_unicode, 
                   load_vocab, 
                   convert_by_vocab, 
                   convert_tokens_to_ids, 
                   convert_ids_to_tokens)

class BertTokenizer(object):

    def __init__(self, 
                 vocab  = None, 
                 do_lower_case = True, 
                 do_basic_tokenize = True, 
                 never_split=["[UNK]", "[SEP]", "[PAD]", "[CLS]", "[MASK]"]):

        self.vocab = load_vocab(vocab)
        self.inv_vocab = {v: k for k, v in self.vocab.items()}
        self.basic_tokenizer = BasicTokenizer(do_lower_case = do_lower_case, never_split = never_split)
        self.wordpiece_tokenizer = WordpieceTokenizer(vocab = self.vocab)
        self.do_basic_tokenize = do_basic_tokenize

    def tokenize(self, text):
        split_tokens = []
        if self.do_basic_tokenize:
            tokens, _ = self.basic_tokenizer.tokenize(text)
            text = " ".join(tokens)
        split_tokens, current_positions = self.wordpiece_tokenizer.tokenize(text)
        return split_tokens, current_positions

    def convert_tokens_to_ids(self, tokens):
        return convert_by_vocab(self.vocab, tokens)

    def convert_ids_to_tokens(self, ids):
        return convert_by_vocab(self.inv_vocab, ids)
