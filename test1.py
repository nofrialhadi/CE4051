pip install torch-summary

import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
#from torchvision import datasets
from torchvision import models
from torchvision.transforms import ToTensor, Normalize, transforms, Resize
from torchsummary import summary
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

