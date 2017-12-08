"""https://www.tensorflow.org/get_started/get_started"""
import tensorflow as tf

NODE1 = tf.constant(3.0, dtype=tf.float32)
NODE2 = tf.constant(4.0)  # also tf.float32 implicitly
NODE3 = tf.add(NODE1, NODE2)
print(NODE3)
SESS = tf.Session()
print(SESS.run(NODE3))
