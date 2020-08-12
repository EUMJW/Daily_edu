import numpy as np

def test_slice(dataset, start, x_shape,y,y_prediction=False):
    x_data = []
    y_data = []
    
    for i in range(start-1,len(dataset)-x_shape[0]-x_shape[1]-y+2):
        xlst=[]
        ylst=[]
        for j in range(x_shape[0]):
            xlst.append(dataset[i+j:i+j+x_shape[1]])
            if y_prediction == False: 
                ylst.append(dataset[i+j+x_shape[1]+2])
        x_data.append(xlst)
        y_data.append(ylst)
    if y_prediction == False:
        return np.array(x_data), np.array(y_data)
    else:
        return np.array(x_data)
