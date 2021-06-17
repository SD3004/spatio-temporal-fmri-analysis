import torch
import torch.nn as nn



class MLP(nn.Module):

    '''
    This class defines a multi-layer perceptrons architecture
    '''

    def __init__(self,input_size,
                      hidden_size = [1024,512,32], 
                      dropout=0.5,
                      bias=False):

        super(MLP,self).__init__()

        self.input_size = input_size
        self.hidden_size = hidden_size
        self.dropout = dropout
        self.num_linear = len(hidden_size)
        self.bias = bias

        ## fully connected layers
        self.fc_layers = torch.nn.ModuleDict()

        self.fc_layers['fc_layer_0'] = nn.Linear(self.input_size, self.hidden_size[0], bias=self.bias)
        for i in range(self.num_linear-1):
            self.fc_layers[f'fc_layer_{i+1}'] = nn.Linear(self.hidden_size[i],self.hidden_size[i+1], bias=self.bias)
        
        ## classification layer
        self.fc_class = nn.Linear(self.hidden_size[-1],1 , bias=self.bias)

        if self.dropout:
            self.dropout = nn.Dropout(self.dropout)

        #init_weights(self)

        ## activation
        self.relu = nn.ReLU()

    def forward(self,x):

        out = x
        for i in range(self.num_linear):
            out = self.fc_layers[f'fc_layer_{i}'](out)
            out = self.relu(out)
        
        if self.dropout:
            out = self.dropout(out)
        out = self.fc_class(out)
        return out