#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/6/10


import tensorflow as tf
import numpy as np
# print(tf.executing_eagerly())


@tf.function
def simple_nn_layer(x,y):
    return tf.nn.relu(tf.matmul(x,y))

x = tf.random.uniform((3,3))
y = tf.random.uniform((3,3))

result = simple_nn_layer(x,y)
print(result)


