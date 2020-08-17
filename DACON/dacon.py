import pandas as pd
import numpy as np
from keras.models import Model
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten
from keras.layers.merge import concatenate
from keras.callbacks import EarlyStopping, ModelCheckpoint


train = pd.read_csv('.data/train.csv')
test = pd.read_csv('.data/test.csv')

x_train = train.iloc[:,1:2]
xl_train = train.iloc[:,2:3]
y_train = train.iloc[:,3:]

xl_train = pd.get_dummies(xl_train)

inputx = Input(shape=(784,))
x = Dense(40, activation = 'relu')(inputx)
x = Dropout(0.2)(x)
x = Dense(20, activation = 'relu')(x)
x = Dropout(0.2)(x)


inputxl = Input(shape=(26,1))


merged_model = concatenate([x,inputxl])

output = Dense(8, activation = 'relu')(merged_model)
output = Dense(4, activation = 'relu')(output)
output = Dense(10, activation = 'softmax')(output)

model = Model(inputs=[input_dnn, input_rnn, input_cnn], outputs=output)



es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=50)
mc = ModelCheckpoint('./best_model.h5', monitor='val_loss', mode='min', save_best_only=True)

model.compile(optimizer='adam', loss = 'mse')
model.fit([x_train, xl_train], y_train, batch_size = 4, epochs = 500, validation_split = 0.2, callbacks=[es, mc])


