
import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = keras.datasets.imdb
(train_data, train_labels), (test_data, test_data) = data.load_data(num_words=10000)
