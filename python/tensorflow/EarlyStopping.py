from tensorflow.keras.callbacks import EarlyStopping

# Crear el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Early Stopping
early_stopping = EarlyStopping(monitor='loss', patience=3)

# Datos sintéticos
import numpy as np
X = np.random.random((1000, 10))
y = np.random.randint(0, 2, 1000)

# Entrenar
model.fit(X, y, epochs=50, batch_size=32, callbacks=[early_stopping])
