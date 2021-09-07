import torch
import os

os.environ['CUDA_LAUNCH_BLOCKING'] = '1'
 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(torch.cuda.get_device_name(device))
