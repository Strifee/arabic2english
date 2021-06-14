'''
 for rtx 30 series : conda install -q pytorch torchvision cudatoolkit=11 -c pytorch-nightly
'''

import pandas as pd
import numpy as np 
from torch import nn
import torch
from torchtext import data
from torch.nn  import functional as F
import torch.optim as  optim 

if torch.cuda.is_available():  
  dev = "cuda:0" 

  print("gpu up")
else:  
  dev = "cpu"  
