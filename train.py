import pandas as pd
import numpy as np 
from torch import nn
import torch
from torchtext import data
from torch.nn  import functional as F
import torch.optim as  optim 
from data_processing import SRC,TARGET
from transformer import Transformer

class Trainer():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    load_model = False
    save_model = True

    #Training hyperparameters
    num_epochs = 5
    learning_rate = 3e-4
    batch_size = 32

    #Model hyperparameters
    src_vocab_size = len(SRC.vocab)
    trg_vocab_size = len(TARGET.vocab)

    embedding_size = 256
    num_heads = 8
    num_encoder_layers = 3
    num_decoder_layers = 3
    max_len= 227
    src_pad_idx =SRC.vocab.stoi["<pad>"]
    
    model = Transformer(
        embedding_size,
        src_vocab_size,
        trg_vocab_size,
        src_pad_idx,
        num_heads,
        num_encoder_layers,
        num_decoder_layers,
        max_len
    ).to(device)