# Spatio-Temporal Deep Learning for fMRI analysis

## Dataset

![alt text](img/connectivity.png "ICA_15 network matrix")


## Tensorboard

To visualise experiments logs in tensorbard run the following line:

``` tensorboard --logdir='./logs/' ```

## Useful Links

Gadgil et al 2020, [Spatio-Temporal Graph Convolution for Functional MRI Analysis](https://github.com/sgadgil6/cnslab_fmri)

## Results

### Sex prediction 

Multi-layer Perceptron (MLP) classifier




| Model | Data | Architecture | Train-accuracy | Validation-accuracy | Remarks |
| ---      |  ------  | ----------| ----------| ----------| --- |
| ST-GCN | cov mat ts - 22 ROIs  |  (64,64,1)  | **0.828**  | **0.752** | 5-folds average |
| ours   | ICA10   | xxx  | xxx   | xxx  | xxx | 
| ours   | ICA25   | xxx  | xxx   | xxx  |  xxx |
| ours   | ICA50   | xxx  | xxx   | xxx  | xxx | 
| ours   | ICA100   | xxx  | xxx   | xxx  | xxx | 
| ours   | ICA200   | xxx  | xxx   | xxx  | xxx|
| ours   | ICA300   | xxx  | xxx   | xxx  | xxx|


### Fluid intelligence prediction 

|  | Train-accuracy | Validation-accuracy |
| ---      |  ------  |----------|
| ICA15   | xxx   | xxx  |
| ICA25   | xxx   | xxx  |
| ICA50   | xxx   | xxx  |
| ICA100   | xxx   | xxx  |
| ICA200   | xxx   | xxx  |
| ICA300   | xxx   | xxx  |


