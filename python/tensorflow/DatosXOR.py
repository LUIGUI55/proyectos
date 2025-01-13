import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Datos de entrenamiento para el problema XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Características
y = np.array([[0], [1], [1], [0]])  # Etiquetas

# Crear el modelo
modelo = Sequential()
modelo.add(Dense(8, input_dim=2, activation='relu'))  # Capa oculta con 8 neuronas
modelo.add(Dense(1, activation='sigmoid'))  # Capa de salida con 1 neurona para clasificación binaria

# Compilar el modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(X, y, epochs=500, verbose=0)

# Hacer predicciones
predicciones = modelo.predict(X)
print(predicciones)


import tensorflow as tf
import numpy as np

# Crear datos sintéticos
X = np.random.random((1000, 5))
y = np.random.randint(0, 2, (1000,))

# Crear el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(5,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X, y, epochs=10, batch_size=32)
