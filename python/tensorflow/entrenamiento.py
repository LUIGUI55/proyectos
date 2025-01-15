import tensorflow as tf

# Dataset sintético
texts = ["esto es un ejemplo", "el modelo aprende bien", "tensorflow es poderoso", "usa embeddings para texto"]
labels = [0, 1, 1, 0]

# Tokenización y preparación de datos
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(texts)
X = pad_sequences(tokenizer.texts_to_sequences(texts), maxlen=10)
y = tf.convert_to_tensor(labels)

# Modelo de clasificación
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(100, 16, input_length=10),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilar y entrenar
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=20, batch_size=2)
