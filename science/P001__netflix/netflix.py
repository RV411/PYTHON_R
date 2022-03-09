import pandas as pd
import seaborn as sns

data=pd.read_csv(r"C:\Users\ivan_\Documents\PYTHON_R\science\P001__netflix\netflix.csv")


########################################################################
########################### Duplicados #################################
########################################################################

data[data.duplicated()]     # Ver duplicados
data.drop.duplicated(inplace=True)      # Eliminar duplicados


########################################################################
data.isnull().sum()             # Suma de nulos
sns.heatmap(data.isnull())      #Grafica de nulos

########################################################################
##      Buscar una palabra en las columnas

data[data['Title'].isin(['House of Cards'])]
data[data['Title'].str.contains('House of Cards')]

########################################################################
##      Grafica de barras de los años en la base de datos

data.dtypes
data['date_N']= pd.to_datetime(data['Release_Date'])
data['date_N'].dt.year.value_counts()
data['date_N'].dt.year.value_counts().plot(kind='bar')

########################################################################
##      Grafica de Categoria

data.groupby('Category').Category.count()
sns.countplot(data['Category'])

########################################################################
##

data['Year']=data['date_N'].dt.year
data[(data['Category']=='Movie') & (data['Year']==2000)]


##  SOlo los titulos
data[(data['Category']=='TV Shows') & (data['Country']=='India')]['Title']


########################################################################
##      Top 10 de Directores

data['Director'].value_counts().head(10)

########################################################################
##      Buscar datos en una columna donde hay datos vacios
#   Se eliminan porque no deja filtrar

data_new=data.dropna()      #Borra filas que contienen missing values
data_new[data_new['Cast'].str.contains('Tom Cruise')]


########################################################################
##      Es importante usar nunique y unique en las columnas para ver si no hay NaN
# Cuando identificamos que datos hay en una columna

data.nunique()
data.unique()


########################################################################
##      Datos en una consulta
# Usar shape

data[(data['Category']=='Movie') & (data['Rating']=='TV-14')|(data['Country']=='Canada')].shape
data[(data['Category']=='Movie') & (data['Rating']=='R')|(data['Year']>2018)].shape

########################################################################
##      Mayor Duracion de una serie
#

data.Duration.unique()      #Ver los tipos de Duraciones
data.Duration.dtypes      #No muestra los tipos

data[['Minutes','Unit']]=data['Duration'].str.split('',expand=True) #   Divide los datos en 2 columnas

data['Minutes'].max()
data['Minutes'].min()

########################################################################
##
#
data_tvshow=data[data['Category']=='TV Show']
data_tvshow.Country.value_counts().head(1)      # El mejor programa de TV Show

