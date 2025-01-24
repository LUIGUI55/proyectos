import tensorflow as tf
import numpy as np

# Crear datos sintéticos
X = np.random.random((1000, 10, 8))  # 1000 secuencias de 10 pasos con 8 características
y = np.random.randint(0, 2, (1000,))

# Crear el modelo RNN
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(32, input_shape=(10, 8)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X, y, epochs=10, batch_size=32)
