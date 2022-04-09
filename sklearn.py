# import pandas as pd
# import numpy as np
# import sklearn
# from sklearn.preprocessing  import MinMaxScaler
# import tensoflow as tf
# from keras.models.models import Sequential
# from keras.models.layers import Dense
# from keras.models.layers import LSTM
# from keras.models.layers import Dropout
# from keras.callbacks.callbacks import ModelCheckpoint
#
# tesla = pd.read_csv('TSLA.csv')
# tesla = tesla[['Date', 'Close']]
# new_tesla = tesla.loc[884:1639]
# new_tesla = new_tesla.drop('Date', axis =1)
# new_tesla.new_tesla.rese_index(drop = True)
# T = T.astype('float32')
# T = np.reshape(T, (-1,1))
# scaler = MinMaxScaler(feature_range =(0,1))
# T = scaler.fit_transform(T)
#
# train_size = int(len() * 0.80)
# test_size = int(len() - train_size)
# train, test = T[0: train_size, :], T[train_size:len(T), :]
#
# def create_features(data, window_size):
# 	x, y = [], []
# 	for i in range(len(data) - window_size -1):
# 		x.append(window)
# 		y.append(data[i + window_size, 0])
# 	return (np.array(x), np.array(y))
#
# 	window = data[i:(i + window_size), 0]
#
# window_size = 20
# x_train, y_train = create_features(train, window_size)
# x_test, y_test = create_features(test, window_size)
#
# x_train = np.reshape(x_train, (x_train.shape[0],1, x_train.shape[1]))
#
# x_test = np.reshape(x_train, (x_test.shape[0],1, x_test.shape[1]))
#
# print(train_size, test_size)
#
#
# # Tensorflow model
# tf.random.set_seed(11)
# np.random.seed(11)
#
# model = Sequential()
# model.add(LSTM(units = 50, activation = 'relu',input_shape = (x_train.shape[1], window_size)))
# model.add(Dropout(0.2))
# model.add(Dense(1))
#
# model.compile(loss = 'mean_squared_error', optimizer ='adam', metrics =['accuracy'])
#
#
# # print(tesla.head())
