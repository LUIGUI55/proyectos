import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard
import datetime

# Crear un directorio para los logs
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

# Crear el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Datos sintéticos
X = tf.random.normal((1000, 10))
y = tf.random.uniform((1000,), maxval=2, dtype=tf.int32)

# Entrenar
model.fit(X, y, epochs=10, callbacks=[tensorboard_callback])

# Ejecutar en la terminal para ver los resultados:
# tensorboard --logdir=logs/fit
