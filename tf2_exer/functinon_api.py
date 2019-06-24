#!/usr/bin/env python
# coding=utf-8
# Project: leetcode
# Author : chenwen_hust@qq.com
# Date   : 2019/6/17

try:
    import tensorflow.python.keras as keras
except:
    import tensorflow.keras as keras


import tensorflow as tf
'''
inputs = keras.Input(shape=(784,),name='img_input')
h1 = keras.layers.Dense(32,activation='relu')(inputs)
h2 = keras.layers.Dense(32,activation='relu')(h1)

outputs = keras.layers.Dense(10,activation='softmax',name='output_results')(h2)
model = keras.Model(inputs,outputs,name='mnist model')

model.summary()

# 训练、验证及测试
(x_train,y_train),(x_test,y_test) = keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1,784).astype('float32')/255
x_test = x_test.reshape(-1,784).astype('float32')/255
model.compile(optimizer=keras.optimizers.RMSprop(),loss='sparse_categorical_crossentropy',metrics=['accuracy'])
history = model.fit(x_train,y_train,batch_size=64,epochs=5,validation_split=0.2)
test_scores = model.evaluate(x_test,y_test,verbose=0)
print(test_scores)

# 模型保存
model.save('model_save.h5')
del model
model = keras.models.load_model('model_save.h5')


# keras.utils.plot_model(model,'mnist_model.png')
# keras.utils.plot_model(model,'model_info.png',show_shapes=True)
'''

'''
encoder_input = keras.Input(shape=(28,28,1),name='img')
h1 = keras.layers.Conv2D(16,3,activation='relu')(encoder_input)
h1 = keras.layers.Conv2D(32,3,activation='relu')(h1)
h1 = keras.layers.MaxPool2D((3,3))(h1)
h1 = keras.layers.Conv2D(32,3,activation='relu')(h1)
h1 = keras.layers.Conv2D(16,3,activation='relu')(h1)
encoder_output = keras.layers.GlobalMaxPool2D()(h1)
encode_model = keras.Model(encoder_input,encoder_output,name='encoder')
encode_model.summary()

h2 = keras.layers.Reshape((4,4,1))(encoder_output)
h2 = keras.layers.Conv2DTranspose(16,3,activation='relu')(h2)
h2 = keras.layers.Conv2DTranspose(32,3,activation='relu')(h2)
h2 = keras.layers.UpSampling2D((3,3))(h2)
h2 = keras.layers.Conv2DTranspose(16,3,activation='relu')(h2)
decode_output = keras.layers.Conv2DTranspose(1,3,activation='relu')(h2)
auto_encoder = keras.Model(encoder_input,decode_output,name='autoencoder')
auto_encoder.summary()
'''

'''
# 多输入与多输出网络
num_words = 2000
num_tags = 12
num_departments=4

# 输入
body_input = keras.Input(shape=(None,),name='body')
title_input = keras.Input(shape=(None,),name='title')
tag_input = keras.Input(shape=(num_tags,),name='tag')

# 嵌入层
body_feat = keras.layers.Embedding(num_words,64)(body_input)
title_feat = keras.layers.Embedding(num_words,64)(title_input)   # 两个embedding实例,分别调用，没有共享权重

# 特征提取层
body_feat = keras.layers.LSTM(32)(body_feat)
title_feat = keras.layers.LSTM(128)(title_feat)
features = keras.layers.concatenate([title_feat,body_feat,tag_input])

# 分类层
priority_pred = keras.layers.Dense(1,activation='sigmoid',name='priority')(features)
department_pred = keras.layers.Dense(num_departments,activation='softmax',name='department')(features)

# 构建模型
model = keras.Model([body_input,title_input,tag_input],[priority_pred,department_pred])
model.summary()
model.compile(optimizer=keras.optimizers.RMSprop(1e-3),
              loss={'priority':'binary_crossentropy','department':'categorical_crossentropy'},
              loss_weights=[1.0,0.2])

import numpy as np
# 数据
title_data = np.random.randint(num_words,size=(1280,10))
body_data = np.random.randint(num_words,size=(1280,100))
tag_data = np.random.randint(2,size=(1280,num_tags)).astype('float32')

# 标签
priority_label = np.random.random(size=(1280,1))
department_label = np.random.randint(2,size=(1280,num_departments))

history = model.fit({'title':title_data,'body':body_data,'tag':tag_data},
                    {'priority':priority_label,'department':department_label},
                    batch_size=32,
                    epochs=5)
'''

'''
# 共享网络层
share_embedding = keras.layers.Embedding(2000,64)
input_1 = keras.Input(shape=(None,),dtype='int32')
input_2 = keras.Input(shape=(None,),dtype='int32')

feat1 = share_embedding(input_1)
feat2 = share_embedding(input_2)
'''

# 模型复用
# from tensorflow.python.keras.applications import VGG16
# vgg16 = VGG16()

# image_input = keras.Input(shape=(32,32,3),name='img_input')
# timeseries_input = keras.Input(shape=(None,10),name='ts_input')
#
# x1 = keras.layers.Conv2D(3,(3,3))(image_input)
# x1 = keras.layers.GlobalMaxPooling2D()(x1)
#
# x2 = keras.layers.Conv1D(3,3)(timeseries_input)
# x2 = keras.layers.GlobalMaxPooling1D(x2)
#
# x = keras.layers.concatenate([x1,x2])
#
# score_output = keras.layers.Dense(1,name='score_output')(x)
# class_output = keras.layers.Dense(5,activation='softmax',name='class_output')(x)
#
# model = keras.Model(input=[image_input,timeseries_input],
#                     outputs=[score_output,class_output])












