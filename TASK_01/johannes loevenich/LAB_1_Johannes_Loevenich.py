# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.chunk import ne_chunk
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

Input = 'input-text.txt'
output1 = 'output_file_1.txt'
output2 = 'output_file_2.txt'

    
def format_output(chunk):

    if type(chunk) is nltk.tree.Tree:
        return '_'.join([x[0] for x in list(chunk)]) + '_NER' 
    elif chunk[1] in ['VERB', 'NOUN']:
        return chunk[0] + '_' + chunk[1].upper()
    return chunk[0]

with open(Input, 'r') as file, open(output1, 'w') as output_file1, open(output2, 'w') as output_file2:
    for line in file:
        tokens = word_tokenize(line)
        without_ner =  [tag for tag in nltk.pos_tag(tokens, tagset='universal')]
        ner =  ne_chunk(without_ner, binary=False)
        output_without =  ' '.join([format_output(chunk) for chunk in without_ner])
        output_ner = ' '.join([format_output(chunk) for chunk in ner])
        output_file1.write(output_without)
        output_file2.write(output_ner)

    print 'format_output completed.'.format(output_file1,output_file2)