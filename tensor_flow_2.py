#from __future__ import print_function

#do this to stop log in terminal saying if you build from source
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf


a = tf.constant(2)
b = tf.constant(3)

#launch the default graph.
with tf.Session() as sess:
    print("a=2, b=3")
    print("Addition with constants: %i" % sess.run(a+b))
    print("Multiplication with constants: %i" % sess.run(a*b))



a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add= tf.add(a,b)
mul = tf.multiply(a,b)

#launch the default graph
with tf.Session() as sess:
    print("addition with variables: %i" % sess.run(add, feed_dict = {a:2,b: 3}))
    print("multiplication with variables: %i" % sess.run(mul, feed_dict = {a:2,b:3}))


#produces a 1x2 matrix
matrix1 = tf.constant([[3.,3.]])

#produces a 2x1 matrix
matrix2 = tf.constant([[2.],[2.]])

product = tf.matmul(matrix1,matrix2)


with tf.Session() as sess:
    result = sess.run(product)
    print(result)




    
