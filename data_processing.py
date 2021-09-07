import pandas as pd
import torch.nn as nn
import random
import re
import spacy
from torchtext.legacy import data
from spacy.tokenizer import Tokenizer
from spacy.lang.ar import Arabic



random.seed(0)
df = pd.read_csv("data/arabic_english.txt",delimiter="\t",names=["eng","ar"])

'''
First :
python -m spacy download en_core_web_sm
'''
spacy_eng = spacy.load("en_core_web_sm")

ar = Arabic()
ar_Tokenizer = Tokenizer(ar.vocab)

def engTokenizer(text):
 return  [word.text for word in spacy_eng.tokenizer(text)] 

def arTokenizer(sentence):
    return  [word.text for word in 
             ar_Tokenizer(re.sub(r"\s+"," ",re.sub(r"[\.\'\"\n+]"," ",sentence)).strip())]

SRC = data.Field(tokenize=engTokenizer,batch_first=False,init_token="<sos>",eos_token="<eos>")
TRG = data.Field(tokenize=arTokenizer,batch_first=False,tokenizer_language="ar",init_token="ببدأ",eos_token="نهها")

class TextDataset(data.Dataset):

    def __init__(self, df, src_field, target_field, is_test=False, **kwargs):
        fields = [('eng', src_field), ('ar',target_field)]
        samples = []
        for i, row in df.iterrows():
            eng = row.eng 
            ar = row.ar
            samples.append(data.Example.fromlist([eng, ar], fields))

        super().__init__(samples, fields, **kwargs)
    
    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        return self.samples[idx]

torchdataset = TextDataset(df,SRC,TRG)

train_data, valid_data = torchdataset.split(split_ratio=0.8, random_state = random.seed(0))

SRC.build_vocab(train_data,min_freq=2)
TRG.build_vocab(train_data,min_freq=2)

if __name__=='__main__':
    print(TRG.vocab.freqs.most_common(50))  

