# Generamos datos artificiales: dos anillos concéntricos.
X, Y = make_circles(n_samples=500, factor=0.5, noise=0.05)

# Resolución del mapa de predicción.
res = 100 

# Coordenadas del mapa de predicción.
_x0 = np.linspace(-1.5, 1.5, res)
_x1 = np.linspace(-1.5, 1.5, res)

# Input con cada combo de coordenadas del mapa de predicción.
_pX = np.array(np.meshgrid(_x0, _x1)).T.reshape(-1, 2)

# Objeto vacío a 0.5 del mapa de predicción.
_pY = np.zeros((res, res)) + 0.5

# Visualización del mapa de predicción y nube de datos.
plt.figure(figsize=(8, 8))
plt.pcolormesh(_x0, _x1, _pY, cmap="coolwarm", vmin=0, vmax=1)
plt.scatter(X[Y == 0,0], X[Y == 0,1], c="skyblue")
plt.scatter(X[Y == 1,0], X[Y == 1,1], c="salmon")
plt.tick_params(labelbottom=False, labelleft=False)

# Importamos TensorFlow y configuramos para usar la versión 1.
import tensorflow.compat.v1 as tf
from matplotlib import animation
from IPython.core.display import display, HTML
tf.disable_v2_behavior()

# Definimos los puntos de entrada de la red, para la matriz X e Y.
iX = tf.placeholder('float', shape=[None, X.shape[1]])
iY = tf.placeholder('float', shape=[None])

# Tasa de aprendizaje y número de neuronas por capa.
lr = 0.01           
nn = [2, 16, 8, 1]  

# Inicializamos pesos y sesgos para cada capa de la red.
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

iPY = [] # Aquí guardaremos la evolución de las predicciones, para la animación.

with tf.Session() as sess:
  
    # Inicializamos todos los parámetros de la red, las matrices W y b.
    sess.run(tf.global_variables_initializer())
    
    # Iteramos n pases de entrenamiento.
    for step in range(n_steps):
  
        # Evaluamos al optimizador, a la función de coste y al tensor de salida pY. 
        # La evaluación del optimizer producirá el entrenamiento de la red.
        _, _loss, _pY = sess.run([optimizer, loss, pY], feed_dict={iX: X, iY: Y})
    
        # Cada 25 iteraciones, imprimimos métricas.
        if step % 25 == 0: 
      
            # Cálculo del accuracy.
            acc = np.mean(np.round(_pY) == Y)
      
            # Impresión de métricas.
            print('Step', step, '/', n_steps, '- Loss = ', _loss, '- Acc =', acc)
      
            # Obtenemos predicciones para cada punto de nuestro mapa de predicción _pX.
            _pY = sess.run(pY, feed_dict={iX: _pX}).reshape((res, res))

            # Y lo guardamos para visualizar la animación.
            iPY.append(_pY)


"""
import pandas as pd

# Cargar datos desde el archivo CSV
df = pd.read_csv('datos.csv')

# Obtener características (X) y etiquetas (Y)
X = df[['feature1', 'feature2']].values
Y = df['label'].values

import pandas as pd

# Cargar datos desde el archivo CSV
df = pd.read_csv('datos.csv')

# Obtener características (X) y etiquetas (Y)
X = df.drop('label', axis=1).values  # Todas las columnas excepto la etiqueta
Y = df['label'].values

import pandas as pd

[
    {"feature1": 0.1, "feature2": 0.2, "label": 0},
    {"feature1": -0.3, "feature2": 0.5, "label": 1},
    ...

    # Cargar datos desde el archivo JSON
    df = pd.read_json('datos.json')

    # Obtener características (X) y etiquetas (Y)
    X = df.drop('label', axis=1).values  # Todas las columnas excepto la etiqueta
    Y = df['label'].values
]

import pandas as pd

# Cargar datos desde el archivo CSV o JSON
df = pd.read_csv('datos.csv')  # o pd.read_json('datos.json')

# Rellenar valores nulos con la media de cada columna
df = df.fillna(df.mean())

# Obtener características (X) y etiquetas (Y)
X = df.drop('label', axis=1).values
Y = df['label'].values

# Resto del código...
En este ejemplo, df.mean() calcula la media de cada columna y fillna() reemplaza los valores nulos con esas medias.

Si prefieres rellenar con otro valor específico, puedes hacerlo así:

python
Copy code
# Rellenar valores nulos con un valor específico (por ejemplo, 0)
df = df.fillna(0)

"""