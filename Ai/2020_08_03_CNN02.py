from keras.models import Sequential
from keras.layers import Dense, LSTM, Activation, Conv2D,MaxPooling2D,Flatten

model = Sequential()
model.add(Conv2D(10,input_shape = (10,10,1), kernel_size=(2,2)))
model.add(Conv2D(10,(3,3)))
# model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(1))

model.summary()