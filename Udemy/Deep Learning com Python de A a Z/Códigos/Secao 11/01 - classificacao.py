from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.layers.normalization import BatchNormalization
from keras.preprocessing.image import ImageDataGenerator

model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(units=128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

generator_train = ImageDataGenerator(rescale=1./255, rotation_range=7, horizontal_flip=True, shear_range=0.2, height_shift_range=0.07, zoom_range=0.2)
generator_test = ImageDataGenerator(rescale = 1./255)

base_train = generator_train.flow_from_directory('dataset/training_set', target_size=(64, 64), batch_size=32, class_mode='binary')
base_test = generator_train.flow_from_directory('dataset/test_set', target_size=(64, 64), batch_size=32, class_mode='binary')

# O mais correto é utilizar steps_per_epoch=4000, para passar 1 por 1
model.fit_generator(base_train, steps_per_epoch=4000/32, epochs = 5, validation_data=base_test, validation_steps=100/32)