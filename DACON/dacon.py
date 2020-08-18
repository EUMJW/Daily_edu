import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

from keras.models import Model
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, Activation, Dropout, BatchNormalization, ELU
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint,ReduceLROnPlateau
from keras.layers.merge import concatenate
from keras import optimizers


# 데이터 전처리

train = pd.read_csv('.data/train.csv')
test = pd.read_csv('.data/test.csv')

x_train = train.iloc[:,3:]
x_train = np.array(x_train).reshape(-1,28,28,1)

y_train = pd.get_dummies(train.digit)
y_train = np.array(y_train)

x_letter_train = pd.get_dummies(train.letter)
x_letter_train = np.array(x_letter_train)


# augmentation

from keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator(
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2)

lst=[]
for i in x_train:
  num = 0
  for batch in datagen.flow(i.reshape(1,28,28,1), batch_size=1):
    lst.append(batch.reshape(28,28,1))
    num +=1
    if num>0:
      break

x_train = np.concatenate((x_train,np.array(lst)),axis=0)
x_letter_train = np.concatenate((x_letter_train,x_letter_train), axis=0)
y_train = np.concatenate((y_train, y_train), axis=0)



# 모델

x_inputs = Input(shape=(28,28,1))
x_letter_inputs = Input(shape=(26,))

x = Conv2D(256,(3,3),activation='elu', padding='same')(x_inputs)
x = Dropout(0.2)(x)
x = MaxPooling2D(2,2)(x)
x = Conv2D(128,(2,2),activation='elu', padding='same')(x)
x = Dropout(0.2)(x)
x = Conv2D(64,(2,2),activation='elu', padding='same')(x)
x = Dropout(0.2)(x)
x = Flatten()(x)

x = Dense(128)(x)
x = Dropout(0.2)(x)
x = Dense(64, activation = 'relu')(x)


from keras.layers.merge import concatenate

merged_model = concatenate([x,x_letter_inputs])

out = Dense(256, activation = 'elu')(merged_model)
out = Dropout(0.2)(out)
out = Dense(256, activation = 'elu')(out)
out = Dropout(0.2)(out)
out = Dense(128, activation = 'elu')(out)
out = Dropout(0.2)(out)
out = Dense(10, activation = 'softmax')(out)

model = Model(inputs=[x_inputs,x_letter_inputs], outputs = out)

model.summary()





# 모델 학습

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=50)
mc = ModelCheckpoint('./best_model.h5', monitor='val_loss', mode='min', save_best_only=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=20, verbose=1, mode='min')

model.compile(optimizer='adam', loss = 'categorical_crossentropy', metrics = ['acc'])
model.fit([x_train, x_letter_train], y_train, batch_size = 16, epochs = 500, validation_split = 0.1, callbacks=[es, mc, reduce_lr])



# 테스트셋
test = pd.read_csv('test.csv')

x_test = test.iloc[:,2:]
x_test = np.array(x_test).reshape(-1,28,28,1)/255

x_letter_test = pd.get_dummies(test.letter)
x_letter_test = np.array(x_letter_test)

pre = model.predict([x_test, x_letter_test], batch_size = 50)

# 서브미션에 저장

lst=[]
for i in range(len(pre)):
  lst.append(np.argmax(pre[i]))

submission.digit = lst

submission.to_csv('submission.csv', mode='w', index=False)
