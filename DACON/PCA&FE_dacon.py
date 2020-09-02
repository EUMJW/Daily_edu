from keras.datasets import mnist
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
import tensorflow as tf
from keras.utils import np_utils

from keras import regularizers
from sklearn.decomposition import PCA


# letter 별로 pca분석, 첫번째 주성분 저장

letter_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

pca_list=[]
for i in range(26):
  letter = train[train.letter == letter_list[i]]
  letter = np.array(letter.iloc[:,3:])/255
  pca = PCA()
  pca = PCA(n_components=1)
  pca_xtrain = pca.fit_transform(letter)
  pca_list.append(pca.components_)


pca_list = np.array(pca_list).reshape(26,784)



# 분석 결과를 시각화

fig, axes = plt.subplots(4, 7, subplot_kw={'xticks': (), 'yticks': ()}) 



for i, (comp, ax) in enumerate(zip(pca_list, axes.ravel())): 

    ax.imshow(comp.reshape(28,28)) 

    ax.set_title(letter_list[i])

plt.gray() # 사진 흑백

plt.show() # 사진 출력


# train셋에서 이미지, digit을 가져옴
x_train = train.iloc[:,3:]

x_train = np.array(x_train).reshape(-1,28,28,1)/255

y_train = pd.get_dummies(train.digit)
y_train = np.array(y_train)

# train셋의 letter를 위에서 만든 pca 첫번째 주성분으로 매핑
x_letter_train=[]
for i in train.letter:
  for j in range(26):
    if i == letter_list[j]:
      x_letter_train.append(pca_list[j])
x_letter_train = np.array(x_letter_train).reshape(-1,28,28,1)

print(x_letter_train.shape)



# 모델
# 실제 그림과 Letter의 이미지(pca 주성분으로 매핑) 을 input으로 하여 CNN
# output은 digit의 onehot

x_inputs = Input(shape=(28,28,1))

x = Conv2D(32,(3,3),padding='same', activation = 'relu')(x_inputs)
x = Dropout(0.4)(x)
x = Conv2D(32,(3,3),padding='same', activation = 'relu')(x)
x = MaxPooling2D((2,2))(x)
x = Conv2D(64,(3,3),padding='same', activation = 'relu')(x)
x = Dropout(0.4)(x)
x = Conv2D(64,(3,3),padding='same', activation = 'relu')(x)
x = MaxPooling2D((2,2))(x)
x = Conv2D(128,(3,3),padding='same', activation = 'relu')(x)
x = Dropout(0.4)(x)
x = Conv2D(128,(3,3),padding='same', activation = 'relu')(x)
x = BatchNormalization()(x)
x = MaxPooling2D((2,2))(x)
x = Flatten()(x)
x = Dense(64, activation= 'relu')(x)

x_letter_inputs = Input(shape=(28,28,1))

xl = Conv2D(32,(3,3),padding='same', activation = 'relu')(x_letter_inputs)
xl = Dropout(0.4)(xl)
xl = Conv2D(32,(3,3),padding='same', activation = 'relu')(xl)
xl = MaxPooling2D((2,2))(xl)
xl = Conv2D(64,(3,3),padding='same', activation = 'relu')(xl)
xl = Dropout(0.4)(xl)
xl = MaxPooling2D((2,2))(xl)
xl = Conv2D(128,(3,3),padding='same', activation = 'relu')(xl)
xl = Dropout(0.4)(xl)
xl = Conv2D(128,(3,3),padding='same', activation = 'relu')(xl)
xl = BatchNormalization()(xl)
xl = MaxPooling2D((2,2))(xl)
xl = Flatten()(xl)
xl = Dense(64, activation= 'relu')(xl)



from keras.layers.merge import concatenate

merged_model = concatenate([x, xl])

out = Dense(256, activation = 'relu')(merged_model)
out = Dropout(0.4)(out)
out = Dense(128, activation = 'relu')(out)
out = Dropout(0.4)(out)
out = Dense(10, activation = 'softmax')(out)

model = Model(inputs=[x_inputs,x_letter_inputs], outputs = out)

model.summary()


# 모델학습
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=50)
mc = ModelCheckpoint('./best_model.h5', monitor='val_loss', mode='min',verbose=1, save_best_only=True)


model.compile(optimizer='adam', loss = 'categorical_crossentropy', metrics = ['acc'])
model.fit([x_train, x_letter_train], y_train, batch_size = 16, epochs = 500, validation_split = 0.1, callbacks=[es, mc])

model.load_weights('best_model.h5')



# test

test = pd.read_csv('test.csv')
submission = pd.read_csv('submission.csv')

# 테스트셋 PCA
pca_list=[]
for i in range(26):
  letter = test[test.letter == letter_list[i]]
  letter = np.array(letter.iloc[:,2:])/255
  pca = PCA()
  pca = PCA(n_components=1)
  pca_xtest = pca.fit_transform(letter)
  pca_list.append(pca.components_)



pca_list = np.array(pca_list).reshape(26,784)

x_letter_test=[]
for i in test.letter:
  for j in range(26):
    if i == letter_list[j]:
      x_letter_test.append(pca_list[j])
x_letter_test = np.array(x_letter_test).reshape(-1,28,28,1)

# x letter 피처변환
x_letter_test=[]
for i in test.letter:
  for j in range(26):
    if i == letter_list[j]:
      x_letter_test.append(pca_list[j])
x_letter_test = np.array(x_letter_test).reshape(-1,28,28,1)

x_test = test.iloc[:,2:]
x_test = np.array(x_test).reshape(-1,28,28,1)/255


# test셋 예측, 저장
pre = model.predict([x_test, x_letter_test], batch_size = 50)
lst=[]
for i in range(len(pre)):
  lst.append(np.argmax(pre[i]))

submission.digit = lst

submission.to_csv('submission.csv', mode='w', index=False)

