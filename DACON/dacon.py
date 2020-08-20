import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split

from keras.models import Model
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, Activation, Dropout, BatchNormalization, ReLU
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint,ReduceLROnPlateau
from keras.layers.merge import concatenate
from keras import optimizers

from google.colab import files
files.upload()


# GOOGLE COLAB을 사용하여 진행

! unzip data.zip


train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')


x_train = train.iloc[:,3:]
x_train = np.array(x_train).reshape(-1,28,28,1)/255

y_train = pd.get_dummies(train.digit)
y_train = np.array(y_train)

x_letter_train = pd.get_dummies(train.letter)
x_letter_train = np.array(x_letter_train)



print(x_train.shape, y_train.shape, x_letter_train.shape)

# augmentation 12배로
from keras.preprocessing.image import ImageDataGenerator
datagen = ImageDataGenerator(
            rotation_range=20,
            zoom_range = 0.1,
            width_shift_range = 0.1,
            height_shift_range = 0.1)


for i in range(len(x_train)):
  num = 0
  for batch in datagen.flow(x_train[i].reshape(1,28,28,1), batch_size=1):
    x_train = np.concatenate((x_train,batch.reshape(1,28,28,1)), axis = 0)
    x_letter_train = np.concatenate((x_letter_train, x_letter_train[i].reshape(1,26)))
    y_train = np.concatenate((y_train, y_train[i].reshape(1,10)), axis=0)
    num +=1
    if num>=12:
      break




print(x_train.shape, y_train.shape, x_letter_train.shape)


# 인풋
x_inputs = Input(shape=(28,28,1))
x_letter_inputs = Input(shape=(26,))

# 이미지 CNN LAYER
x = Conv2D(32,(3,3),padding='same', activation = 'relu')(x_inputs)
x = Dropout(0.2)(x)
x = Conv2D(32,(3,3),padding='same')(x)
x = BatchNormalization()(x)
x = ReLU()(x)
x = MaxPooling2D((2,2))(x)
x = Conv2D(64,(3,3),padding='same', activation = 'relu')(x)
x = Dropout(0.2)(x)
x = Conv2D(64,(3,3),padding='same')(x)
x = BatchNormalization()(x)
x = ReLU()(x)
x = MaxPooling2D((2,2))(x)
x = Conv2D(128,(3,3),padding='same')(x)
x = Dropout(0.2)(x)
x = Conv2D(128,(3,3),padding='same')(x)
x = BatchNormalization()(x)
x = ReLU()(x)
x = MaxPooling2D((2,2))(x)
x = Flatten()(x)
x = Model(inputs=x_train, outputs = x)

# 문자 DNN LAYER
y = Dense(128, activaion = 'relu')(x_letter_inputs)
y = Dropout(0.2)(y)
y = Dense(64, activation = 'relu')(y)
y = Dropout(0.2)(y)
y = Dense(64, activaion = 'relu')(y)
y = Model(inputs = x_letter_train, outputs = y)


from keras.layers.merge import concatenate

# CONCAT
merged_model = concatenate([x.output, y.output])

out = Dense(256, activation = 'relu')(merged_model)
out = Dropout(0.3)(out)
out = Dense(128, activation = 'relu')(out)
out = Dropout(0.3)(out)
out = Dense(10, activation = 'softmax')(out)

model = Model(inputs=[x_inputs,x_letter_inputs], outputs = out)

model.summary()



es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=30)
mc = ModelCheckpoint('./best_model.h5', monitor='val_loss', mode='min', save_best_only=True)

# 모델학습
model.compile(optimizer='adam', loss = 'categorical_crossentropy', metrics = ['acc'])
model.fit([x_train, x_letter_train], y_train, batch_size = 16, epochs = 500, validation_split = 0.1, callbacks=[es, mc])


test = pd.read_csv('test.csv')
submission = pd.read_csv('submission.csv')

# 서브밋
x_test = test.iloc[:,2:]
x_test = np.array(x_test).reshape(-1,28,28,1)/255

x_letter_test = pd.get_dummies(test.letter)
x_letter_test = np.array(x_letter_test)


print(x_test.shape, x_letter_test.shape)

pre = model.predict([x_test, x_letter_test], batch_size = 50)


lst=[]
for i in range(len(pre)):
  lst.append(np.argmax(pre[i]))


submission.digit = lst
submission.to_csv('submission.csv', mode='w', index=False)

