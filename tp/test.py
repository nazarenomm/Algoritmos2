import numpy as np

dias = np.arange(30)

indices = np.random.choice(dias, size=100)

tasa_likes = 50 * np.exp(-0.1 * dias)

muestra = tasa_likes[indices] # muestra?
Y = np.random.poisson(muestra, size=100) # MUESTRA

print(Y)