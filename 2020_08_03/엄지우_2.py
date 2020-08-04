from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Activation
import numpy as np
import tensorflow as tf

x_data = np.array([1,2,3,4,5,6,7,8,9,10])
y_data = np.array([1,2,3,4,5,1,2,3,4,5])

x_train = x_data[:8]
x_test = x_data[8:]

y_train = y_data[:8]
y_test = y_data[8:]

model = Sequential()
model.add(Dense(10, input_dim= 1, activation = 'relu'))
model.add(Dense(10, activation = 'relu'))
model.add(Dense(6, activation = 'softmax'))

model.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam', metrics=['accuracy'])
model.fit(x_train, y_train, validation_split = 0.2, batch_size =8,  epochs=100)

lose_and_metrics = model.evaluate(x_test, y_test, batch_size = 1)
print(lose_and_metrics)

y_predict = model.predict(x_test)
prediction = [int(tf.argmax(i)) for i in y_predict]

print(prediction)