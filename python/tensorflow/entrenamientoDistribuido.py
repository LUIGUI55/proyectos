import tensorflow as tf

strategy = tf.distribute.MirroredStrategy()

with strategy.scope():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Datos sintéticos
import numpy as np
X = np.random.random((1000, 10))
y = np.random.randint(0, 2, 1000)

# Entrenar el modelo
model.fit(X, y, epochs=10, batch_size=32)
