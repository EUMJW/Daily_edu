from keras.models import Model
from keras.layers import Dense, LSTM, Conv2D, Activation, Dropout, Flatten, MaxPooling2D, Input
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split



from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

scaler = MinMaxScaler()
data = scaler.fit_transform(cancer.data)

x_train, x_test, y_train, y_test = train_test_split(data, cancer.target, test_size=0.2, random_state=5)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

input = Input(shape=(30,))
x = Dense(40, activation = 'relu')(input)
x = Dropout(0.2)(x)
x = Dense(20, activation = 'relu')(x)
x = Dropout(0.2)(x)
x = Dense(1, activation = 'sigmoid')(x)
model = Model(input,x)
model.summary()

model.compile(optimizer='adam', loss = 'binary_crossentropy', metrics = ['acc'])
model.fit(x_train, y_train, batch_size = 16, epochs = 30, validation_split = 0.2)

loss, acc = model.evaluate(x_test, y_test, batch_size = 16)

print(f'test_loss : {loss} , test_acc : {acc}')

y_predict = model.predict(x_test)

print([[y_test[i], round(float(y_predict[i]))] for i in range(len(x_test))])