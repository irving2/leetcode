#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/6/24


import os
from tensorflow.python import keras

check_path = '106save/model.ckpt'
check_dir = os.path.dirname(check_path)

from sklearn.ensemble import VotingClassifier



