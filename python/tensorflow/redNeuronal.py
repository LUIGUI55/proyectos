import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Crear el modelo secuencial
modelo = Sequential()

# Agregar una capa densa (capa completamente conectada)
modelo.add(Dense(10, activation='relu', input_shape=(5,)))  # Capa de entrada con 5 características
modelo.add(Dense(1, activation='sigmoid'))  # Capa de salida para clasificación binaria

# Compilar el modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Resumen del modelo
modelo.summary()


# Crear un modelo secuencial
model = Sequential([
    Dense(10, activation='relu', input_shape=(5,)),
    Dense(1, activation='sigmoid')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Ver resumen del modelo
model.summary()


