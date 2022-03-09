import numpy as np

################################################################################
###########################     OPERATIONS    ##################################
################################################################################

#x=list(range(22))
x=np.arange(1,21)
#y= [[1,2,3],[4,5,6],[7,8,9]]
y=np.arange(10).reshape(3,3)

np.array(y)
np.zeros((3,3)) -5  # Matriz de zeros se le añade -5
np.ones((3,4))      # Hace una matriz de 3x4
np.eyes(4)          # Hace una matriz de diagonal de 4 unos

np.arrange(50).reshape(5,10)    #Hace una matriz de 5 filas 10 colums del 0 al 50

#divicion de una linea
np.linspace(0,100,5)        #[0,25,50,75,100]

#Random
np.random.randn(5)  #5 numeros random negativos y positivos
np.random.randint(5)#5 numeros random enteros

x.min()
x.argmin()      #regresa el indice donde esta el numero minimo

x[:10]  #1 al 9
x[10:]  #11 al 20


x[1:4,2:4]  # toma valores de la fila 1 hasta antes de la 4
            #                 columna 2  hasta antes de la 4


################################################################################
################################################################################
################################################################################


################################################################################
###########################    DOCUMENTATION  ##################################
################################################################################

#https://numpy.org/devdocs/user/basics.html
