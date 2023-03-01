import numpy as np
import matplotlib.pyplot as plt
#definir constantes massa sol em kg, distancia entre marte e o sol
# excentricidade da orbita de Marte

M= 1.989e30
a=227.9e9
e=0.0934
G = 6.673*(10**-11)

#gerar valores para anomalia verdadeira(posição angular de mare em sua orbita)
E=np.linspace(0, 2*np.pi, 100)
M= E - e*np.sin(E)

#Equação de Kepler para a distancia entre marte e o sol
r= a*(1-e*np.cos(E))

#calcular a velocidade orbital de marte usando a equação abaixo
v=np.sqrt(M*G*(1+e)/(a*(1-e)))

# calcular as coordenadas x e y de marte em relação a terra

x=r*np.cos(E)
y=r*np.sin(E)

#plotar a orbita de marte usando o Matplotlib
plt.plot(x,y)
plt.axis('equal')
plt.show()