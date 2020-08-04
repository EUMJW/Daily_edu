import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

x = [[[i],[i+1],[i+2],[i+3]] for i in range(1,7)]
x_data = np.array(x)
y_data = np.array([5,6,7,8,9,10])

x_train = x_data[:5]
x_test = x_data[5:]

y_train = y_data[:5]
y_test = y_data[5:]

model = Sequential()
model.add(LSTM(10, activation='relu',return_sequences=True, input_shape=(4,1)))
model.add(LSTM(10, activation='relu'))
model.add(Dense(1))

model.compile( loss = 'mse', optimizer = 'adam')
model.fit(x_train, y_train, validation_split = 0.2, epochs=100)

mse = model.evaluate(x_test, y_test, batch_size = 1)
print(mse)

y_predict = model.predict(x_test)
y_predict
