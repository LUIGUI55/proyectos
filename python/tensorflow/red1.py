# crearemos una red neuronal con una capa oculta
# y una capa de salida
# usaremos el optimizador Adam
# usaremos el dataset MNIST
# usaremos la funcion de activacion relu

import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

# cargamos el dataset
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
def init_weights(shape):
    return tf.Variable(tf.random_normal(shape, stddev=0.01))
    def model(X, w_h, w_o):
        h = tf.nn.relu(tf.matmul(X, w_h))
        return tf.matmul(h, w_o)
    X = tf.placeholder("float", [None, 784])
    Y = tf.placeholder("float", [None, 10])
    w_h = init_weights([784, 625])
    w_o = init_weights([625, 10])
    py_x = model(X, w_h, w_o)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=py_x, labels=Y))
    train_op = tf.train.AdamOptimizer(0.001).minimize(cost)
    predict_op = tf.argmax(py_x, 1)
    sess = tf.Session()
    init = tf.global_variables_initializer()
    sess.run(init)
    for i in range(100):
        for start, end in zip(range(0, len(mnist.train.images), 128), range(128, len(mnist.train.images)+1, 128)):
            sess.run(train_op, feed_dict={X: mnist.train.images[start:end], Y: mnist.train.labels[start:end]})
        print(i, np.mean(np.argmax(mnist.test.labels, axis=1) == sess.run(predict_op, feed_dict={X: mnist.test.images})))

        \end{lstlisting}
\end{frame}
\begin{frame}[fragile]
    \frametitle{Red neuronal con una capa oculta}
    \begin{lstlisting}
