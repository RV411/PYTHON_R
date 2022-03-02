#html5          pip install html5lib
#x=pd.read_csv('uno.csv')
#x=pd.read_html('https://github.com/uno.csv')


################################################################################
###########################     OPERATIONS    ##################################
################################################################################


import numpy as np
import pandas as pd


x=['a','b','c','d','e']
# y=['1','1','1','1','1']
y=['1','2','3','4','5']
z={1:'a',2:'b',3:'c',4:'d',5:'e'}

#a=pd.Series(data=x,index=y)     # 1:'a',1:'b',1:'c',1:'d',1:'e'
a=pd.Series(y,x)     # 'a':1,'b':2,'c':3,'d':4,'e':5
b=pd.Series(y,x)     # 'a':1,'b':2,'c':3,'d':4,'e':5
print(a+b)           # 'a':2,'b':4,'c':6,'d':8,'e':10

#DATAFRAMES
A=np.arange(0,5)
B=np.arange(5,10)
C=np.arange(10,15)
D=np.arange(15,20)
E=np.arange(20,25)
df=pd.DataFrame([A,B,C,D,E],['a','b','c','d','e'],['W','X','Y','Z']) # a-e columnas   &    W-Z filas

df['P']=df['Y']+df['Z'] # añade una columna P con el valor de la suma

df.drop('e', inplace=True) # Borra definitivamente index e
df.drop('P', axis=1, inplace=True) # Borra definitivamente axis P

df.loc('a','W') # Encuentra la localización del numero
df.loc('a') # Muestra toda la fila del indice


#view dataframes
df[df['W']>3][['W','S']]    # Se muestran filas con el valor mayor a 3 en la columna W
                            # pero solo se muestra las columnas W y S


df[(df['W']>3 | df['Z']>0)]    # Funciona como el if tambien se puede usar => & 


# Filtro de valor
df.dropna(thresh=3)            # Valores de la tabla mayores a 3


#Llenar valores con un valor
df['b'].fillna(value= df['b'].mean())      #llenas los valores con el promedio de la columna


#Agrupa y muestra el promedio
x=df.groupby('item')
x.describe()
x.transpose()



#MERGE
# pd.merge(df1,df2,how='left',on='key')
pd.merge(df1,df2,how='left',on=['key1','key2'])




#Especiales

def funcion_incrementar(lm):
    lm=lm+100
    return lm

x['b'].apply(funcion_incrementar)   #aplica una funcion


x.sort_values('b')    #Ordena por valor

x['b'].unique()     #Encuentra valores unicos en la columna
x['b'].nunique()     #Enumera los valores unicos en la columna
x['b'].value_counts()     #Agrupa y enumera los valores de la columna
x['b'].isnull()     #Cuenta los valores vacios en la columna


################################################################################
################################################################################
################################################################################


################################################################################
###########################    DOCUMENTATION  ##################################
################################################################################

#https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html
