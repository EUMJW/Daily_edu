import numpy as np
from keras.layers import Dense, LSTM, Activation, Dropout
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping,ModelCheckpoint,ReduceLROnPlateau
from slice_1_ejw import test_2_slice


dataset = np.array(range(1,118))


x,y = test_slice(dataset,1,(3,7),3)


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