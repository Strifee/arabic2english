import numpy as np
import torch
from torch import optim
from torch import nn
from torchtext.legacy import data
from data_processing import SRC,TRG
from transformer import Transformer
from device import device
from data_processing import train_data, valid_data 
from hyper_parameters import BATCH_SIZE, embedding_size, src_pad_idx, num_heads, num_encoder_layers, num_decoder_layers, forward_expansion, dropout, max_len, learning_rate, num_epochs

train_iter, valid_iter = data.BucketIterator.splits(
    (train_data,valid_data), 
    batch_size = BATCH_SIZE,
    sort=None,
    sort_within_batch=False,
    sort_key=lambda x: len(x.eng),
    device = device,
    shuffle=True
)

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

loss_track = []
loss_validation_track= []


optimizer = optim.Adam(model.parameters(), lr=learning_rate)

pad_idx = SRC.vocab.stoi["<pad>"]
criterion = nn.CrossEntropyLoss(ignore_index = pad_idx)
for epoch in range(num_epochs):
    stepLoss=[]
    model.train()
    for batch  in train_iter:
        input_data = batch.eng.to(device)
        target = batch.ar.to(device)

        output = model(input_data,target[:-1])
        optimizer.zero_grad()
        
        output = output.reshape(-1,trg_vocab_size)
        target = target[1:].reshape(-1)

        loss = criterion(output,target)
        loss.backward()

        optimizer.step()
        stepLoss.append(loss.item())

    loss_track.append(np.mean(stepLoss))
    print(" Epoch {} | Train Cross Entropy Loss: ".format(epoch),np.mean(stepLoss))
    with torch.no_grad():    
      stepValidLoss=[]
      model.eval() # the evaluation mode for the model (doesn't apply dropout and batchNorm)
      for i,batch  in enumerate(valid_iter):
            input_sentence = batch.eng.to(device)
            target = batch.ar.to(device)
            optimizer.zero_grad()
            output = model(input_sentence,target[:-1])
            output = output.reshape(-1,trg_vocab_size)
            target = target[1:].reshape(-1)
            loss = criterion(output,target)
                  
            stepValidLoss.append(loss.item())
    
    loss_validation_track.append(np.mean(stepValidLoss))
    print(" Epoch {} | Validation Cross Entropy Loss: ".format(epoch),np.mean(stepValidLoss))   