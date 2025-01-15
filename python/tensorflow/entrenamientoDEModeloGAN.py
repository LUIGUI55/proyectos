import tensorflow as tf

# Cargar el dataset Iris
dataset = tf.keras.utils.get_file(
    'iris.data', 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
)

import pandas as pd
data = pd.read_csv(dataset, header=None)
data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
data['class'] = data['class'].astype('category').cat.codes

X = data.iloc[:, :-1].values
y = data['class'].values

# Crear el modelo
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compilar y entrenar
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=50, batch_size=16)
