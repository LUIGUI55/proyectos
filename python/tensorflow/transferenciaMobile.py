import tensorflow as tf
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D

# Cargar MobileNet preentrenado
base_model = MobileNet(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Congelar capas del modelo base
for layer in base_model.layers:
    layer.trainable = False

# Añadir capas personalizadas
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(10, activation='softmax')(x)

# Crear el modelo final
model = Model(inputs=base_model.input, outputs=predictions)

# Compilar el modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import numpy as np

# Generador
def construir_generador():
    modelo = Sequential()
    modelo.add(Dense(128, input_dim=100, activation='relu'))
    modelo.add(Dense(784, activation='sigmoid'))
    return modelo

# Discriminador
def construir_discriminador():
    modelo = Sequential()
    modelo.add(Dense(128, input_dim=784, activation='relu'))
    modelo.add(Dense(1, activation='sigmoid'))
    return modelo

# Crear el modelo GAN
generador = construir_generador()
discriminador = construir_discriminador()

# Crear el modelo de GAN
discriminador.compile(loss='binary_crossentropy', optimizer=Adam(), metrics=['accuracy'])
discriminador.trainable = False
gan = Sequential()
gan.add(generador)
gan.add(discriminador)

# Compilar el modelo GAN
gan.compile(loss='binary_crossentropy', optimizer=Adam())

# Entrenamiento simple del GAN
# Este es un ejemplo básico. Un GAN requiere un entrenamiento más complejo.

