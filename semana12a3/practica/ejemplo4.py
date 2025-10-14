import tensorflow as tf
from tensorflow import keras
from keras import layers
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images.reshape(-1, 28, 28, 1) / 255.0
test_images = test_images.reshape(-1, 28, 28, 1) / 255.0

clases = ["T-shirt/top","Trouser","Pullover","Dress","Coat",
          "Sandal","Shirt","Sneaker","Bag","Ankle boot"]

modelo = keras.Sequential([
    layers.Conv2D(32, (3,3), activation="relu", input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3,3), activation="relu"),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax")
])

modelo.compile(optimizer="adam",
               loss="sparse_categorical_crossentropy",
               metrics=["accuracy"])

modelo.fit(train_images, train_labels, epochs=5, validation_split=0.1)


imagen = Image.open("vestido2.png").convert("L").resize((28, 28))
imagen_array = np.array(imagen) / 255.0
imagen_array = imagen_array.reshape(1,28,28,1)

prediccion = modelo.predict(imagen_array)
indice = np.argmax(prediccion)
probabilidad = np.max(prediccion)

plt.imshow(imagen_array[0,:,:,0], cmap="gray")
plt.title(f"Predicción: {clases[indice]} ({probabilidad:.2f})")
plt.axis("off")
plt.show()
