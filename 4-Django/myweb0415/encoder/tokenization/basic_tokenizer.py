
"""BasicTokenizer classes."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .utils import (convert_to_unicode,
                   clean_text,
                   split_on_whitespace,
                   split_on_punctuation,
                   tokenize_chinese_chars,
                   strip_accents)

class BasicTokenizer(object):
    """Runs basic tokenization (punctuation splitting, lower casing, etc.)."""

    def __init__(self, 
                 do_lower_case=True,
                 never_split=("[UNK]", "[SEP]", "[PAD]", "[CLS]", "[MASK]")):
        """Constructs a BasicTokenizer.
        Args:
          do_lower_case: Whether to lower case the input.
        """
        self.do_lower_case = do_lower_case
        self.never_split = never_split

    def tokenize(self, text):
        """Tokenizes a piece of text."""
        text = convert_to_unicode(text)
        text = clean_text(text)
        text = tokenize_chinese_chars(text)
        # This was added on November 1st, 2018 for the multilingual and Chinese
        # models. This is also applied to the English models now, but it doesn't
        # matter since the English models were not trained on any Chinese data
        # and generally don't have any Chinese data in them (there are Chinese
        # characters in the vocabulary because Wikipedia does have some Chinese
        # words in the English Wikipedia.).
        orig_tokens = split_on_whitespace(text)
        split_tokens = []
        current_positions = []
        for token in orig_tokens:
            if self.do_lower_case and token not in self.never_split:
                token = token.lower()
                token = strip_accents(token)
            current_positions.append([])
            current_positions[-1].append(len(split_tokens))
            split_tokens.extend(split_on_punctuation(token))
            current_positions[-1].append(len(split_tokens))
        return split_tokens, current_positions
