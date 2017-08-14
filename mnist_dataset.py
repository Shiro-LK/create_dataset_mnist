# -*- coding: utf-8 -*-
"""
Save dataset mnist in .jpg
Two folders : train and test with their labels in train.txt and test.txt

@author: shiro
"""
from keras.datasets import mnist
import cv2
import os

def SaveImagesMNIST():
    # Create directory where to save the training images
    directory = 'mnist_dataset/train/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Create directory where to save the testing images
    directory2 = 'mnist_dataset/test/'
    if not os.path.exists(directory2):
        os.makedirs(directory2)
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    
    # Save images and labels : train
    f = open('mnist_dataset/train.txt', 'w')
    
    for i in range(0, len(y_train)):
        cv2.imwrite(directory+'mnist_train_' + str(i) + '.jpg', x_train[i])
        f.write(directory+'mnist_train_' + str(i) + '.jpg' + ' ' + str(y_train[i]) + '\n')
    f.close()
    
    # Save images and labels : test
    f = open('mnist_dataset/test.txt', 'w')
    
    for i in range(0, len(y_test)):
        cv2.imwrite(directory2+'mnist_test_' + str(i) + '.jpg', x_test[i])
        f.write(directory2+'mnist_test_' + str(i) + '.jpg' + ' ' + str(y_test[i]) + '\n')
    f.close()
    
SaveImagesMNIST()
