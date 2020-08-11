import numpy as np
from keras.layers import Dense, LSTM, Activation, Dropout
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping,ModelCheckpoint,ReduceLROnPlateau

dataset = np.array(range(1,118))

def test_2_slice(dataset, start, x_shape,y,y_prediction=False):
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

x,y = test_2_slice(dataset,1,(3,7),3)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

model = Sequential()
model.add(LSTM(30, input_shape = (3,7)))
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(3))
model.summary()

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=50)
mc = ModelCheckpoint('./best_model.h5', monitor='val_loss', mode='min', save_best_only=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=20, verbose=1, mode='min')



model.compile(optimizer='adam', loss = 'mse')
model.fit(x_train,y_train,epochs=500,validation_split=0.2,batch_size=1,
            verbose=2,callbacks=[es, mc,reduce_lr])

loss = model.evaluate(x_test,y_test)

x_hat = test_2_slice(dataset,109, (3,7) , 0 , y_prediction=True)

y_predict = model.predict(x_hat)


print(f'test loss :    {loss}')
print(f'y_predict :   {y_predict}')