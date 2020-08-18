from keras.models import Model
from keras.layers import Dense, LSTM, Conv2D, Activation, Dropout, Flatten, MaxPooling2D, Input
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from keras.callbacks import EarlyStopping, ModelCheckpoint


diabetes = datasets.load_diabetes()


x_train, x_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.1, random_state=5)

dx_train = x_train
dx_test = x_test
rx_train =  x_train.reshape(-1,2,5)
rx_test =  x_test.reshape(-1,2,5)
cx_train = x_train.reshape(-1,2,5,1)
cx_test = x_test.reshape(-1,2,5,1)


# dnn 모델
input_dnn = Input(shape=(10,))
dnn_layer = Dense(64, activation = 'relu')(input_dnn)
dnn_layer = Dropout(0.2)(dnn_layer)
dnn_layer = Dense(32, activation = 'relu')(dnn_layer)
dnn_layer = Dropout(0.2)(dnn_layer)
dnn_layer = Dense(16, activation = 'relu')(dnn_layer)
dnn_layer = Dropout(0.2)(dnn_layer)
dnn_layer = Dense(1)(dnn_layer)

# rnn 모델

input_rnn = Input(shape=(2,5))
rnn_layer = LSTM(10)(input_rnn)
rnn_layer = Dense(5, activation = 'relu')(rnn_layer)
rnn_layer = Dense(1)(rnn_layer)

# cnn 모델

input_cnn = Input(shape=(2,5,1))
cnn_layer = Conv2D(10, (2,2))(input_cnn)
cnn_layer = Flatten()(cnn_layer)
cnn_layer = Dense(5, activation = 'relu')(cnn_layer)
cnn_layer = Dense(1)(cnn_layer)

# 앙상블

from keras.layers.merge import concatenate

merged_model = concatenate([dnn_layer,rnn_layer,cnn_layer])

output = Dense(8)(merged_model)
output = Dense(4)(output)
output = Dense(1)(output)

model = Model(inputs=[input_dnn, input_rnn, input_cnn], outputs=output)


model.summary()


# 모델학습

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=50)
mc = ModelCheckpoint('./best_model.h5', monitor='val_loss', mode='min', save_best_only=True)

model.compile(optimizer='adam', loss = 'mse')
model.fit([dx_train, rx_train, cx_train], y_train, batch_size = 4, epochs = 500, validation_split = 0.2, callbacks=[es, mc])



# 모델평가
mse = model.evaluate([dx_test,rx_test,cx_test],y_test)
print('loss   :   ',mse)


y_predict = model.predict([dx_test,rx_test,cx_test])

for i in range(len(y_test)):
  print('real Y : ', y_test[i],'       y_predict : ', float(y_predict[i]))