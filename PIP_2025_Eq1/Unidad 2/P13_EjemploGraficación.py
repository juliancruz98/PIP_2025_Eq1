# y = mx + b
x = [i for i in range(-5,6,1)]
print(x)

m = 3
b = 2


#
y = [i*m+b for i in x]
print(y)

from matplotlib import pyplot as plt
plt.plot(x,y, marker="x",linestyle ="--" ,color = "#42CC99")
plt.show()

#PRACTICA 4 = Probar otras maneras de personalizar el diseño de las graficas con mathplotlib