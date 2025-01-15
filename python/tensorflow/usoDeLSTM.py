import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb

# Cargar datos de IMDb
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=10000)

# Rellenar secuencias para que todas tengan la misma longitud
X_train = pad_sequences(X_train, maxlen=500)
X_test = pad_sequences(X_test, maxlen=500)

# Crear el modelo LSTM
modelo = Sequential()
modelo.add(Embedding(input_dim=10000, output_dim=128, input_length=500))
modelo.add(LSTM(128, return_sequences=False))
modelo.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
modelo.fit(X_train, y_train, epochs=5, batch_size=64)

# Evaluar el modelo
test_loss, test_acc = modelo.evaluate(X_test, y_test, verbose=2)
print('\nPrecisión en los datos de prueba:', test_acc)
