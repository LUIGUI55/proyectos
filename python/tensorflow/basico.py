import tensorflow as tf

# Crear un tensor con valores definidos
tensor = tf.constant([1, 2, 3, 4])
print(tensor)


# Crear un tensor
tensor = tf.constant([[1, 2], [3, 4]], dtype=tf.float32)

# Operaciones con tensores
print(tensor)
print("Suma: ", tf.reduce_sum(tensor))
print("Forma: ", tensor.shape)