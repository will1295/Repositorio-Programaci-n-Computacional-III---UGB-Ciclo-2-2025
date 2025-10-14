import tensorflow as tf
import keras
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

fashion_mnist = keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()

train_images = train_images/255.0
test_images = test_images/255.0

clases = ["T-shirt/top","Trouser","Pullover","Dress","Coat",
          "Sandal","Shirt","Sneaker","Bag","Ankle boot"]

modelo = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation="relu"),
    keras.layers.Dense(10,activation="softmax")
])

modelo.compile(optimizer="adam",
               loss="sparse_categorical_crossentropy",
               metrics=["accuracy"])

modelo.fit(train_images,train_labels,epochs=5)

predicciones = modelo.predict(test_images)
print("Prediccion: ",clases[np.argmax(predicciones[0])])

plt.figure()
plt.imshow(test_images[0])
plt.colorbar()
plt.grid(False)
plt.title(f"Prediccion: {clases[np.argmax(predicciones[0])]}")
plt.show()



