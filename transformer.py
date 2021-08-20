from torch import nn
import torch
from device import device

class Transformer(nn.Module):
    def __init__(
        self,
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
    ):
        super(Transformer, self).__init__()
        self.src_embeddings = nn.Embedding(src_vocab_size,embedding_size)
        self.src_positional_embeddings= nn.Embedding(max_len,embedding_size)
        self.trg_embeddings= nn.Embedding(trg_vocab_size,embedding_size)
        self.trg_positional_embeddings= nn.Embedding(max_len,embedding_size)
        self.device = device
        self.transformer = nn.Transformer(
            embedding_size,
            num_heads,
            num_encoder_layers,
            num_decoder_layers,
            forward_expansion,
            dropout,
        )

        self.fc_out = nn.Linear(embedding_size, trg_vocab_size)
        self.dropout = nn.Dropout(dropout)
        self.src_pad_idx = src_pad_idx
    
    def make_src_mask(self, src):
        src_mask = src.transpose(0,1) == self.src_pad_idx

        return src_mask

    def forward(self,src,trg):
        src_seq_length, S = src.shape
        trg_seq_length, S = trg.shape
        #adding zeros is an easy way
        src_positions = (
            torch.arange(0, src_seq_length).unsqueeze(1).expand(src_seq_length, S).to(self.device)
        )
        
        
        trg_positions = (
            torch.arange(0, trg_seq_length).unsqueeze(1).expand(trg_seq_length, S).to(self.device)
        )

        embed_src  = self.dropout(
                ( self.src_embeddings(src) + self.src_positional_embeddings(src_positions) )
            )

        embed_trg = self.dropout(
                ( self.trg_embeddings(trg) + self.trg_positional_embeddings(trg_positions) )
            )
        
        src_padding_mask = self.make_src_mask(src)
        trg_mask = self.transformer.generate_square_subsequent_mask(trg_seq_length).to(device)
        
        
        out = self.transformer(embed_src,embed_trg, src_key_padding_mask=src_padding_mask,tgt_mask=trg_mask )
        out= self.fc_out(out)

        return out
        