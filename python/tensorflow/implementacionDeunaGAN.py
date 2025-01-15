import tensorflow as tf
from tensorflow.keras.layers import Dense, LeakyReLU, Input
from tensorflow.keras.models import Sequential

# Generador
generator = Sequential([
    Dense(128, activation='relu', input_dim=100),
    Dense(256, activation='relu'),
    Dense(512, activation='relu'),
    Dense(784, activation='tanh')
])

# Discriminador
discriminator = Sequential([
    Dense(512, input_dim=784),
    LeakyReLU(0.2),
    Dense(256),
    LeakyReLU(0.2),
    Dense(1, activation='sigmoid')
])

# Compilar discriminador
discriminator.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# GAN combinada
discriminator.trainable = False
gan_input = Input(shape=(100,))
x = generator(gan_input)
gan_output = discriminator(x)
gan = tf.keras.models.Model(gan_input, gan_output)

gan.compile(optimizer='adam', loss='binary_crossentropy')

# Entrenamiento ficticio
import numpy as np
noise = np.random.normal(0, 1, (1000, 100))
fake_data = generator.predict(noise)
