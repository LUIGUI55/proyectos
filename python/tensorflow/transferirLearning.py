import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Cargar el modelo VGG16 preentrenado
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Congelar las capas base
base_model.trainable = False

# Crear el modelo completo
modelo = Sequential()
modelo.add(base_model)
modelo.add(Flatten())
modelo.add(Dense(512, activation='relu'))
modelo.add(Dense(1, activation='sigmoid'))  # Para clasificación binaria

# Compilar el modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Resumen del modelo
modelo.summary()
