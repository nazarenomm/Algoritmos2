import numpy as np

array = np.arange(30)

otroArray = np.random.choice(array, size=30)

tasa_likes = 50 * np.exp(-0.1 * array) # es un array que contiene los likes por dia

muestra = tasa_likes[otroArray]

print()
