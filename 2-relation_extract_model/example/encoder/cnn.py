import torch
import torch.nn as nn
import torch.nn.functional as F

class CNN(nn.Module):

    def __init__(self, input_size=50, hidden_size=256, dropout=0, kernel_size=3, padding=1, activation_function=F.relu):
        """
        Args:
            input_size: dimention of input embedding
            kernel_size: kernel_size for CNN
            padding: padding for CNN
            hidden_size: hidden size
        """
        super().__init__()
        self.conv = nn.Conv1d(input_size, hidden_size, kernel_size, padding=padding)
        self.act = activation_function
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        # Check size of tensors
        x = x.transpose(1, 2) 
        x = self.conv(x) 
        x = self.act(x) 
        x = self.dropout(x) 
        x = x.transpose(1, 2) 
        return x
