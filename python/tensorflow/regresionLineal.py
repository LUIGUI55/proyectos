import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Datos de entrenamiento
X = np.array([[1], [2], [3], [4], [5]])  # Características
y = np.array([1, 2, 3, 4, 5])  # Etiquetas (en este caso, una regresión simple)

# Crear el modelo
modelo = Sequential()
modelo.add(Dense(1, input_dim=1))  # Una capa con 1 neurona (regresión lineal)

# Compilar el modelo
modelo.compile(optimizer='adam', loss='mean_squared_error')

# Entrenar el modelo
modelo.fit(X, y, epochs=500, verbose=0)

# Hacer predicciones
predicciones = modelo.predict(X)
print(predicciones)


import tensorflow as tf

# Cargar el conjunto de datos MNIST
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalizar los datos
x_train = x_train / 255.0
x_test = x_test / 255.0

# Crear el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(x_train, y_train, epochs=5)

# Evaluar el modelo
model.evaluate(x_test, y_test)




