from sklearn.model_selection import train_test_split

from keras.models import Model
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, Activation, Dropout, BatchNormalization, ReLU
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint,ReduceLROnPlateau
from keras.layers.merge import concatenate
from keras import optimizers
import tensorflow as tf

from sklearn.decomposition import PCA

# y, x_letter
y_train = pd.get_dummies(train.digit)
y_train = np.array(y_train)

x_letter_train = pd.get_dummies(train.letter)
x_letter_train = np.array(x_letter_train)


# 이미지는 PCA로 차원축소
pca = PCA()
x_train = np.array(train.iloc[:,3:])

# x_train의 pixel값이 175를 넘는것은 1, 이하는 0으로

x_train[x_train<=175]=0
x_train[x_train>0]=1

pca.fit(x_train)
cumsum = np.cumsum(pca.explained_variance_ratio_)
d = np.argmax( cumsum >= 0.95) +1

pca = PCA(n_components=d)
pca_xtrain = pca.fit_transform(x_train)

print(pca_xtrain.shape)

x_test = np.array(test.iloc[:,2:])
x_test[x_test<=175]=0
x_test[x_test>0]=1
pca_xtest = pca.fit_transform(x_test)

print(pca_xtest.shape)


# 모델

x_inputs = Input(shape=(241,))
x = Dense(128, activation = 'relu')(x_inputs)
x = Dropout(0.2)(x)
x = Dense(64, activation = 'relu')(x)
x = Dropout(0.2)(x)
x = Dense(64, activation = 'relu')(x)


x_letter_inputs = Input(shape=(26,))
y = Dense(128, activation = 'relu')(x_letter_inputs)
y = Dropout(0.2)(y)
y = Dense(64, activation = 'relu')(y)
y = Dropout(0.2)(y)
y = Dense(64, activation = 'relu')(y)



from keras.layers.merge import concatenate

merged_model = concatenate([x, y])

out = Dense(256, activation = 'relu')(merged_model)
out = Dropout(0.3)(out)
out = Dense(128, activation = 'relu')(out)
out = Dropout(0.3)(out)
out = Dense(10, activation = 'softmax')(out)

model = Model(inputs=[x_inputs,x_letter_inputs], outputs = out)

model.summary()



# 모델학습

es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=50)
mc = ModelCheckpoint('./best_model.h5', monitor='val_loss', mode='min',verbose=1, save_best_only=True)


model.compile(optimizer='adam', loss = 'categorical_crossentropy', metrics = ['acc'])
model.fit([pca_xtrain, x_letter_train], y_train, batch_size = 16, epochs = 500, validation_split = 0.1, callbacks=[es, mc])



# 결과 - val_loss: 1.6402 - val_acc: 0.4390 전처리 후 조금 나아졌다