from __future__ import absolute_import, division, print_function

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

def load_and_prepare_FMNIST():
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    train_images = train_images / 255.0
    test_images = test_images / 255.0

    return (train_images, train_labels), (test_images, test_labels)

def define_model():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.softmax)
    ])

    model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

    return model

# хочу следить за обучением он-лайн. Можно написать через декораторы
(train_images, train_labels), (test_images, test_labels) = load_and_prepare_FMNIST()
model = define_model()
model.fit(train_images, train_labels, epochs=25)
test_loss, test_acc = model.evaluate(test_images, test_labels)
train_loss, train_acc = model.evaluate(train_images, train_labels)
print('Test accuracy:', test_acc)
print('Train accuracy:', train_acc)

predictions = model.predict(test_images)

Теория по ML: https://ranalytics.github.io/data-mining/044-Ensembles.html