import tensorflow as tf
# constant makes a constant tensor (in this case a rank 0 tensor because its scalar
hello = tf.constant('Hello Machine Learning')
# sess is a class to run tensorflow operations
sess = tf.Session()
sess.run(hello)
#making another rank 0 tensor then running it with session
a = tf.constant(10)
b = tf.constant(32)
sess.run(a+b)
