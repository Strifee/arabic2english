import torch
from data_processing import SRC,TRG
from transformer import Transformer

class Trainer():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    load_model = False
    save_model = True

    num_epochs = 40
    learning_rate = 0.0003

    num_heads = 8
    num_encoder_layers = 3
    num_decoder_layers = 3

    max_len= 230
    dropout = 0.10
    embedding_size= 256
    src_pad_idx = SRC.vocab.stoi["<pad>"]
    forward_expansion = 4
    step = 0


    src_vocab_size  = len(SRC.vocab)
    print("Size of english vocabulary:",src_vocab_size)

    #No. of unique tokens in label
    trg_vocab_size =len(TRG.vocab)
    print("Size of arabic vocabulary:",trg_vocab_size)


    model = Transformer(        
        embedding_size,
        src_vocab_size,
        trg_vocab_size,
        src_pad_idx,
        num_heads,
        num_encoder_layers,
        num_decoder_layers,
        forward_expansion,
        dropout,
        max_len,
        device,
    ).to(device)