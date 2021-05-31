# Spatio-Temporal Deep Learning for fMRI analysis

## Dataset

![alt text](img/connectivity.png "ICA_15 network matrix")


## Tensorboard

To visualise experiments logs in tensorbard run the following line:

``` tensorboard --logdir='./logs/' ```

## Useful Links

ST-GCN - Gadgil et al 2020, [Spatio-Temporal Graph Convolution for Functional MRI Analysis](https://github.com/sgadgil6/cnslab_fmri)

## Results

### Sex classification 

Multi-layer Perceptron (MLP) classifier




| Model | Data | Input Features | Architecture | Train-accuracy | Validation-accuracy | Remarks |
| ------ |  ----| --  | ----------| ----------| ----------| --- |
| ST-GCN | cov matrix - **22** ROIs  | 253 |  (64,64,1)  | **0.828**  | **0.752** | 5-folds average, SGD 1e-2 |
| ours   | ICA15   | 105 |(64,64,1)   | **1.00**   | **0.847**  | dropout 0.5, Adam 1e-4 | 
| ours   | ICA25   | 300 | (64,64,1)   | **1.00**    | **0.835**  |  same |
| ours   | ICA50   | 1225 | (64,64,1)   | **1.00**    | **0.902**  | same | 
| ours   | ICA100   | 4950 | (64,64,1)   | **1.00**    | **0.961**  | same | 
| ours   | ICA200   | 19900 | (64,64,1)   | **1.00**    | **0.957**  | same |
| ours   | ICA300   | 44850 | (64,64,1)   | **1.00**    | **0.968**  | same |


### Fluid intelligence prediction 

|  | Train-accuracy | Validation-accuracy |
| ---      |  ------  |----------|
| ICA15   | xxx   | xxx  |
| ICA25   | xxx   | xxx  |
| ICA50   | xxx   | xxx  |
| ICA100   | xxx   | xxx  |
| ICA200   | xxx   | xxx  |
| ICA300   | xxx   | xxx  |


