
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 00:37:48 2019

@author: OMEN
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Imports
import numpy as np
import tensorflow as tf
import os
import cv2
from segmentation import GetInputData
tf.logging.set_verbosity(tf.logging.INFO)

# Our application logic will be added here



def cnn_model_fn(features, labels, mode):
    input_layer = tf.reshape(features["x"], [-1, 28, 28, 1])
    conv_1 = tf.layers.conv2d(
      inputs=input_layer,
      filters=32,
      kernel_size=[5, 5],
      padding="same",
      activation=tf.nn.relu)
    pool_1 = tf.layers.max_pooling2d(inputs=conv_1,
                            pool_size = [2,2],
                            strides = 2)
    conv_2 = tf.layers.conv2d(
      inputs=pool_1,
      filters=64,
      kernel_size=[5, 5],
      padding="same",
      activation=tf.nn.relu)    
    pool_2 = tf.layers.max_pooling2d(inputs = conv_2,
                            pool_size = [2,2],
                            strides = 2)
    dropout = tf.layers.dropout(
      inputs = pool_2,
      rate = 0.8,
      training=mode == tf.estimator.ModeKeys.TRAIN)
    flatten = tf.contrib.layers.flatten(inputs = dropout)
    dense_1 = tf.layers.dense(inputs = flatten,
                              units = 1024,
                              activation = tf.nn.relu)  
    logits = tf.layers.dense(inputs = dense_1,
                             units = 10)
    
    predictions = {
            "classes": tf.argmax(input = logits, axis = 1),
            "probabilites": tf.nn.softmax(logits, name = "softmax_tensor")}

    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)
    loss = tf.losses.sparse_softmax_cross_entropy(labels = labels, logits = logits)

    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
        train_op = optimizer.minimize(
            loss=loss,
            global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)
    eval_metric_ops = {"accuracy": tf.metrics.accuracy(labels=labels, predictions=predictions["classes"]), 
                       "precision": tf.metrics.precision(labels=labels, predictions=predictions["classes"]),
                       #"f1 score": tf.metrics.f1_score(labels=labels, predictions=predictions["classes"]),
#                       "TP" :tf.metrics.true_positives(labels=labels, predictions=predictions["classes"]),
#                       "TN" :tf.metrics.true_negatives(labels=labels, predictions=predictions["classes"]),
                    
                       }
    return tf.estimator.EstimatorSpec(mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)

def LoadData(path):
    data = []
    labels = []
    for file in os.listdir(path):
        I = np.float32(cv2.imread(path + file, cv2.IMREAD_GRAYSCALE))
        data.append(np.reshape(I, (I.shape[0] * I.shape[1]))/255)
        labels.append(np.int32(file[-5]))
    data = np.asarray(data)
    labels = np.asarray(labels)
    return data, labels
    
    
def main(unused_argv):
  # Load training and eval data
  mnist = tf.contrib.learn.datasets.load_dataset("mnist")
  train_data = mnist.train.images # Returns np.array
  train_labels = np.asarray(mnist.train.labels, dtype=np.int32)
  eval_data = mnist.test.images # Returns np.array
  # Get data from input image
  file = 'input//006.jpg'
  GetInputData(file)
  eval_labels = np.asarray(mnist.test.labels, dtype=np.int32)
  #Create the estimator
  mnist_classifier = tf.estimator.Estimator(model_fn=cnn_model_fn, model_dir="/tmp/mnist_convnet_model_v2.1")
  # Set up logging for predictions
  tensors_to_log = {"probabilities": "softmax_tensor"}
  logging_hook = tf.train.LoggingTensorHook(tensors=tensors_to_log, every_n_iter=50)
  train_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"x": train_data},
    y=train_labels,
    batch_size=1,
    num_epochs=None,
    shuffle=True)
  mnist_classifier.train(
    input_fn=train_input_fn,
    steps=100,
    hooks=[logging_hook])
 
  eval_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": eval_data}, y=eval_labels, num_epochs=1, shuffle=False)  
  
  print(eval_input_fn)
  eval_results = mnist_classifier.evaluate(input_fn=eval_input_fn)
  print(eval_results)
#  saver = tf.train.Saver()
#  save_path = saver.save(mnist_classifier , "/tmp/model.ckpt")
  #%%
    # Load data for prediction
  predict_data, labels = LoadData('output//')
  predict_input_fn = tf.estimator.inputs.numpy_input_fn(
          x = {"x": predict_data},
          shuffle=False)
  predict_reuslt = mnist_classifier.predict(input_fn = predict_input_fn)
  i = 0 
  print("labels  -> predictions")
  
  for result in list(predict_reuslt):
       print(str(labels[i]) + " -> " + str(result["classes"]))
       i += 1
       
  text_file = open("Output.txt", "w+")
  for result in list(predict_reuslt):
      text_file.write((str(result["classes"])))
       
  eval_input_fn_custom = tf.estimator.inputs.numpy_input_fn(
        x={"x": predict_data}, y=labels, num_epochs=1, shuffle=False) 
  eval_results = mnist_classifier.evaluate(input_fn=eval_input_fn_custom)
  print(eval_results)

  
if __name__ == "__main__":
    tf.app.run()
    