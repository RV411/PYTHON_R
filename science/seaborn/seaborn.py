import seaborn as sns
import numpy as np
import pandas as pd

tips = sns.load_dataset('tips')
tips.head()
#sns.displot(tips['total_bill'])
# sns.residplot(x='total_bill',y='tip',data=tips)
# sns.jointplot(x='total_bill',y='tip',data=tips)
#sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex',color='#4CB391') # kind='kde' reg

x=sns.pairplot(tips,hue='day')
x.map_diag(sns.displot)
x.map_upper(sns.kdeplot)


dots = sns.load_dataset('dots')
dots.head()
sns.pairplot(dots,hue='choice')


################################################################################
###########################     CATEGORICAL   ##################################
################################################################################

#diference by two categories        
sns.countplot(x='smoker',data=tips)
sns.factorplot(x='smoker',y='tip',data=tips,kind='bar') #kind='box point'
sns.swarmplot(x='smoker',y='tip',data=tips, hue='sex',palette='cool') #palette='coolwarm magma'
sns.stripplot(x='smoker',y='tip',data=tips, hue='sex',palette='cool') #palette='coolwarm magma'

sns.barplot(x='day',y='tip',data=tips,palette='cool') # hue='sex'   palette='coolwarm magma'
sns.boxplot(x='day',y='tip',data=tips,palette='cool') # hue='sex'   palette='coolwarm magma'
sns.violinplot(x='day',y='tip',data=tips,palette='cool') # hue='sex'   palette='coolwarm magma'


#
sns.pointplot(x='total_bill',y='day',data=tips)

################################################################################
###########################       heatmap     ##################################
################################################################################

tips2=tips.corr()      #meters
sns.heatmap(tips2,annot=True,lw=3,linecolor='black',cmap='cool')


################################################################################
###########################     presentation  ##################################
################################################################################

sns.countplot(x='smoker',data=tips)
sns.set_context('notebook')#paper poster        amplia la imagen de la grafica
sns.despine(left=True,bottom=True,top=False)    #quita el margen del a grafica
sns.set_style('darkgrid')   #whitegrid  ticks


################################################################################
###########################    DOCUMENTATION  ##################################
################################################################################

#https://seaborn.pydata.org/examples/index.html



