from keras.models import Sequential
from keras.layers import Dense, LSTM, Conv2D, Activation, Dropout, Flatten, MaxPooling2D
from keras.callbacks import EarlyStopping,ModelCheckpoint
from keras.datasets import mnist
from keras.utils import np_utils
import numpy as np


(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(-1,28,28,1)/255
x_test = x_test.reshape(-1,28,28,1)/255

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

model = Sequential()
model.add(Conv2D(10,(3,3),input_shape = (28,28,1), padding='same'))
model.add(MaxPooling2D((2,2)))
model.add(Flatten())
model.add(Dense(10, activation = 'softmax'))

model.summary()

model.compile(optimizer='adam', loss = 'categorical_crossentropy', metrics = ['acc'])
model.fit(x_train, y_train, batch_size = 32, epochs = 10, validation_split = 0.2)

loss, acc = model.evaluate(x_test, y_test, batch_size = 32)

print(f'test_loss : {loss} , test_acc : {acc}')

y_predict = model.predict(x_test)

print([[[np.argmax(y_test[i])],[np.argmax(y_predict[i])]] for i in range(len(y_test))])

