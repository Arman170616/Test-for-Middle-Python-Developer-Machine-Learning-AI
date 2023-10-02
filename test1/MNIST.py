import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Load the MNIST dataset
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)), 
    keras.layers.Dense(128, activation='relu'), 
    keras.layers.Dropout(0.2),  
    keras.layers.Dense(10)  
])

model.compile(
    optimizer='adam',
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), 
    metrics=['accuracy']
)



num_epochs = 10

history = model.fit(
    train_images, 
    train_labels, 
    epochs=num_epochs, 
    validation_data=(test_images, test_labels)
)


test_loss, test_accuracy = model.evaluate(test_images, test_labels, verbose=2)
print("\nTest accuracy:", test_accuracy)


plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()



#Kaggle link
#https://www.kaggle.com/code/arman170616/train-mnist-neural-network 