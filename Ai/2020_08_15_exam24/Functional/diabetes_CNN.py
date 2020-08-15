from keras.models import Model
from keras.layers import Dense, LSTM, Conv2D, Activation, Dropout, Flatten, MaxPooling2D
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from keras.callbacks import EarlyStopping, ModelCheckpoint

diabetes = datasets.load_diabetes()


x_train, x_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.1, random_state=5)

x_train = x_train.reshape(-1,2,5,1)
x_test = x_test.reshape(-1,2,5,1)

input = Input(shape=(2,5,1))
x = Conv2D(10, (2,2))(input)
x = Flatten()(x)
x = Dense(5, activation = 'relu')(x)
x = Dense(1)(x)
model = Model(input,x)
model.summary()


es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=50)
mc = ModelCheckpoint('./best_model.h5', monitor='val_loss', mode='min', save_best_only=True)

model.compile(optimizer='adam', loss = 'mse')
model.fit(x_train, y_train, batch_size = 4, epochs = 500, validation_split = 0.2, callbacks=[es, mc])

mse = model.evaluate(x_test,y_test)
print('loss   :   ',mse)

y_predict = model.predict(x_test)

for i in range(len(x_test)):
  print('real Y : ', y_test[i],'       y_predict : ', float(y_predict[i]))
  