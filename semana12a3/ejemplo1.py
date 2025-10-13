import tensorflow as tf
import keras
import matplotlib.pyplot as plt

(x_train,y_train),(x_test,y_test) = keras.datasets.mnist.load_data()

x_train = x_train/255.0
x_test = x_test/255.0

plt.figure(figsize=(5,5))

#for i in range(9):
#    plt.subplot(3,3,i+1)
#    plt.imshow(x_train[i].reshape(28,28),cmap='gray')
#    plt.title(f"Etiqueta: {y_train[i]}")
#    plt.axis("off")
#plt.show()

model = keras.Sequential([
    keras.layers.Conv2D(32,(3,3),activation="relu",input_shape=(28,28,1)),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Conv2D(64,(3,3),activation="relu"),
    keras.layers.MaxPooling2D((2,2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128,activation="relu"),
    keras.layers.Dropout(0,5),
    keras.layers.Dense(10,activation="softmax")
])
model.summary()

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

history = model.fit(
    x_train,y_train,
    validation_split=0.1,
    epochs=5,
    batch_size=64
)

test_loss,test_acc = model.evaluate(x_test,y_test)
print("Precision de los datos de prueba", test_acc)

predicciones = model.predict(x_test[:5])

for i in range(5):
    plt.imshow(x_test[i].reshape(28,28),cmap="gray")
    plt.title(f"Dato dado: {y_test[i]} Prediccion: {predicciones[i].argmax()}")
    plt.axis("off")
    plt.show()












