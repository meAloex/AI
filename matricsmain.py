from keras.datasets import mnist
(train_images,  train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.shape)
(60000, 28, 28)

print(train_images.dtype)

digit = train_images[4]

import matplotlib.pyplot as plt
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()

my_slice = train_images[10:100]
print(my_slice.shape)