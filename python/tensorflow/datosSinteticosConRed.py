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
