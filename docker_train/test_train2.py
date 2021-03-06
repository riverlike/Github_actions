import tensorflow as tf
import argparse

parser = argparse.ArgumentParser(description='Argparse Tutorial')

parser.add_argument('--hidden_units', type=int, 
                help='hidden_units for Dense layer')
args = parser.parse_args()

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
tf.keras.layers.Flatten(input_shape=(28, 28)),
tf.keras.layers.Dense(args.hidden_units, activation='relu'),
tf.keras.layers.Dropout(0.2),
tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

print( '-'*50 )
model.evaluate(x_test,  y_test, verbose=2)
print( '-'*50 )

#action의 워크플로이후에도 모델이 남도록하는 처리 - 단. 깃헙Action의 폴더와 도커허브의 폴더를 매칭.
model.save('/models/saved_model')
