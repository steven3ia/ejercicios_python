#!/usr/bin/env python3

import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles

# Creamos nuestros datos artificiales, donde buscaremos clasificar 
# dos anillos concéntricos de datos. 
X, Y = make_circles(n_samples=500, factor=0.5, noise=0.05)

# Resolución del mapa de predicción.
res = 100 

# Coordendadas del mapa de predicción.
_x0 = np.linspace(-1.5, 1.5, res)
_x1 = np.linspace(-1.5, 1.5, res)

# Input con cada combo de coordenadas del mapa de predicción.
_pX = np.array(np.meshgrid(_x0, _x1)).T.reshape(-1, 2)

# Objeto vacio a 0.5 del mapa de predicción.
_pY = np.zeros((res, res)) + 0.5

# Visualización del mapa de predicción.
plt.figure(figsize=(8, 8))
plt.pcolormesh(_x0, _x1, _pY, cmap="coolwarm", vmin=0, vmax=1)

# Visualización de la nube de datos.
plt.scatter(X[Y == 0,0], X[Y == 0,1], c="skyblue")
plt.scatter(X[Y == 1,0], X[Y == 1,1], c="salmon")

plt.tick_params(labelbottom=False, labelleft=False)

import tensorflow.compat.v1 as tf
from matplotlib import animation
from IPython.core.display import display, HTML

tf.disable_v2_behavior()

# Definimos los puntos de entrada de la red, para la matriz X e Y.
iX = tf.placeholder('float', shape=[None, X.shape[1]])
iY = tf.placeholder('float', shape=[None])

lr = 0.01           # learning rate
nn = [2, 16, 8, 1]  # número de neuronas por capa.

# Capa 1
W1 = tf.Variable(tf.random_normal([nn[0], nn[1]]), name='Weights_1')
b1 = tf.Variable(tf.random_normal([nn[1]]), name='bias_1')

l1 = tf.nn.relu(tf.add(tf.matmul(iX, W1), b1))

# Capa 2
W2 = tf.Variable(tf.random_normal([nn[1], nn[2]]), name='Weights_2')
b2 = tf.Variable(tf.random_normal([nn[2]]), name='bias_2')

l2 = tf.nn.relu(tf.add(tf.matmul(l1, W2), b2))

# Capa 3
W3 = tf.Variable(tf.random_normal([nn[2], nn[3]]), name='Weights_3')
b3 = tf.Variable(tf.random_normal([nn[3]]), name='bias_3')

# Vector de predicciones de Y.
pY = tf.nn.sigmoid(tf.add(tf.matmul(l2, W3), b3))[:, 0]

# Evaluación de las predicciones.
loss = tf.losses.mean_squared_error(pY, iY)

# Definimos al optimizador de la red, para que minimice el error.
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.05).minimize(loss)

n_steps = 1000 # Número de ciclos de entrenamiento.

iPY = [] # Aquí guardaremos la evolución de las predicción, para la animación.

with tf.Session() as sess:
  
  # Inicializamos todos los parámetros de la red, las matrices W y b.
  sess.run(tf.global_variables_initializer())
    
  # Iteramos n pases de entrenamiento.
  for step in range(n_steps):
  
    # Evaluamos al optimizador, a la función de coste y al tensor de salida pY. 
    # La evaluación del optimizer producirá el entrenamiento de la red.
    _, _loss, _pY = sess.run([optimizer, loss, pY], feed_dict={ iX : X, iY : Y })
    
    # Cada 25 iteraciones, imprimimos métricas.
    if step % 25 == 0: 
      
      # Cálculo del accuracy.
      acc = np.mean(np.round(_pY) == Y)
      
      # Impresión de métricas.
      print('Step', step, '/', n_steps, '- Loss = ', _loss, '- Acc =', acc)
      
      # Obtenemos predicciones para cada punto de nuestro mapa de predicción _pX.
      _pY = sess.run(pY, feed_dict={ iX : _pX }).reshape((res, res))

      # Y lo guardamos para visualizar la animación.
      iPY.append(_pY)
      










      
"""
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# Definición de la arquitectura de la red neuronal.
def build_neural_network(input_dim, hidden_layers):
    layers = []

    # Capa de entrada
    layers.append(tf.placeholder('float', shape=[None, input_dim]))

    # Capas ocultas
    for i, layer_size in enumerate(hidden_layers):
        weights = tf.Variable(tf.random_normal([layers[i].shape[1], layer_size]), name=f'Weights_{i + 1}')
        bias = tf.Variable(tf.random_normal([layer_size]), name=f'bias_{i + 1}')
        layer_output = tf.nn.relu(tf.add(tf.matmul(layers[i], weights), bias))
        layers.append(layer_output)

    # Capa de salida
    output_weights = tf.Variable(tf.random_normal([layers[-1].shape[1], 1]), name='Weights_output')
    output_bias = tf.Variable(tf.random_normal([1]), name='bias_output')
    output_layer = tf.nn.sigmoid(tf.add(tf.matmul(layers[-1], output_weights), output_bias))[:, 0]

    return layers[0], output_layer

# Parámetros de la red
input_dim = X.shape[1]
hidden_layers = [16, 8]  # Número de neuronas en cada capa oculta

# Construcción de la red neuronal
iX, pY = build_neural_network(input_dim, hidden_layers)

# Definición de la función de pérdida y el optimizador
iY = tf.placeholder('float', shape=[None])
loss = tf.losses.mean_squared_error(pY, iY)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.05).minimize(loss)

# Resto del código de entrenamiento y animación...
"""