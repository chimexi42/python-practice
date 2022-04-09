import tensorflow as tf
from tensorflow import keras
import os
import matplotlib.pyplot as plt
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# mnist = tf.keras.datasets.mnist

# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# print(x_train.shape)
# print(y_train.shape)
#
# print(x_test.shape)
# print(y_test.shape)

# plt.imshow(x_train[0], cmap = plt.cm.binary)
# plt.show()

data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal',
               'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# train_images = train_images/255.0
# test_images = test_images/255.0

print(train_labels[6])
print(train_images[0])


# plt.imshow(train_images[7], cmap = plt.cm.binary)
# plt.show()




