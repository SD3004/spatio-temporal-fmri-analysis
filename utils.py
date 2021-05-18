import os
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

import torch
import torch.nn as nn


from torch.utils.data import TensorDataset, DataLoader




##### TRAINING #####    

class dataLoaderICA():


    def __init__(self, 
                 data_path,
                 nbr_components,
                 batch_size,
                 num_workers=8,
                 label='sex',
                 random_seed=42,
                  ):
        '''
        This class is the dataloader for the connectivity data
        '''

        self.batch_size = batch_size
        self.num_workers = num_workers
        self.data_path = os.path.join(data_path, 'ICA{}/connectivity_ICA{}.csv'.format(nbr_components,nbr_components))
        self.label = label

        # load csv

        df = pd.read_csv(self.data_path)

        # create two arrays X, y 

        X = df.iloc[:,:-2].values
        y = df[self.label].values

        # split array into train and test
        X_train, X_val, y_train, y_val = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=random_seed, 
                                                        stratify=y)
        print('shape X train {} , y train {}'.format(X_train.shape, y_train.shape))
        print('shape X val {} , y val {}'.format(X_val.shape, y_val.shape))

        # convert into tensors

        self.tensor_x_train = torch.Tensor(X_train)
        self.tensor_y_train = torch.Tensor(y_train)

        self.tensor_x_val = torch.Tensor(X_val)
        self.tensor_y_val = torch.Tensor(y_val)


    
    def getDatasets(self,):

        train_dataset = TensorDataset(self.tensor_x_train,self.tensor_y_train)
        val_dataset = TensorDataset(self.tensor_x_val,self.tensor_y_val)

        return train_dataset, val_dataset

    
    def getDataLoaders(self,):

        train_dataset,val_dataset = self.getDatasets()

        train_loader = torch.utils.data.DataLoader(train_dataset,
                                                   batch_size=self.batch_size,
                                                   shuffle=True,
                                                   num_workers = self.num_workers)
        valid_loader = torch.utils.data.DataLoader(val_dataset,
                                                   batch_size=self.batch_size,
                                                   shuffle=False,
                                                   num_workers = self.num_workers)

        return {"train":train_loader,"valid":valid_loader}

    
    def getInfoDataset(self,):
        
        return 0


##### LOGGING #####    