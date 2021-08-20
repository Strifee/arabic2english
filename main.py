'''
 for rtx 30 series : conda install -q pytorch torchvision cudatoolkit=11 -c pytorch-nightly
'''

import torch

 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

