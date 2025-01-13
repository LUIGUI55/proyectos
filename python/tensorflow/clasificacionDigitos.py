import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

# Cargar los datos de MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocesamiento: normalizar y convertir las etiquetas en formato categórico
X_train = X_train / 255.0
X_test = X_test / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Crear el modelo
modelo = Sequential()
modelo.add(Flatten(input_shape=(28, 28)))  # Aplanar las imágenes 28x28
modelo.add(Dense(128, activation='relu'))
modelo.add(Dense(10, activation='softmax'))  # 10 clases de salida

# Compilar el modelo
modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(X_train, y_train, epochs=5, batch_size=32)

# Evaluar el modelo
test_loss, test_acc = modelo.evaluate(X_test, y_test, verbose=2)
print('\nPrecisión en los datos de prueba:', test_acc)


# Guardar el modelo
model.save('modelo_mnist.h5')

# Cargar el modelo
nuevo_modelo = tf.keras.models.load_model('modelo_mnist.h5')
nuevo_modelo.summary()
