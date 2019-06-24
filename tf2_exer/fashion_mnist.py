#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/6/21


import tensorflow as tf
from tensorflow.python.keras import layers

import numpy as np

# name = 'binaRy crossentropy'
# print(name.title())

from tensorflow import feature_column
feature_columns = []

# numeric cols
# for header in ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'slope', 'ca']:
#     feature_columns.append(feature_column.numeric_column(header))
#
# print(feature_columns[0])

# indicator cols
# thal = feature_column.categorical_column_with_vocabulary_list(
#       'thal', ['fixed', 'normal', 'reversible'])
# thal_one_hot = feature_column.indicator_column(thal)
# feature_columns.append(thal_one_hot)
#
# print(thal_one_hot)






