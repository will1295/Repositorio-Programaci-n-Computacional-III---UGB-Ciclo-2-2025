import tensorflow as tf
import keras as ks
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

mnist = ks.datasets.mnist

imagen = Image.open("mi_numero.png").convert("L")
imagen = imagen.resize((28,28))

imagen_array = np.array(imagen)
imagen_array = imagen_array/255.0
imagen_array = np.expand_dims(imagen_array,axis=0)


(train_images,train_labels),(test_images,test_labels) = mnist.load_data()

train_images = train_images/255.0
test_images = test_images/255.0

modelo = ks.Sequential([
    ks.layers.Flatten(input_shape=(28,28)),
    ks.layers.Dense(128,activation="relu"),
    ks.layers.Dense(10,activation="softmax")
])

modelo.compile(optimizer="adam",
               loss="sparse_categorical_crossentropy",
               metrics=["accuracy"])

modelo.fit(train_images,train_labels,epochs=10)

test_loss,test_acc = modelo.evaluate(test_images,test_labels)
print("Precision del modelo: ",test_acc)

predicciones = modelo.predict(imagen_array)
#indice = 0
resultado = np.argmax(predicciones)
#print("Etiqueta a predecir: ",test_labels[indice])
#print("Prediccion: ",np.argmax(predicciones[indice]))

#plt.figure()
#plt.imshow(test_images[indice])
#plt.title(f"Prediccion: {np.argmax(predicciones[indice])}")
#plt.axis("off")
#plt.show()

plt.figure(figsize=(3,3))
plt.imshow(imagen_array[0],cmap="gray")
plt.title(f"Prediccion: {resultado}")
plt.axis("off")
plt.show()






