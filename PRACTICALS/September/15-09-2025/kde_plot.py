import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("dark")
iris = sns.load_dataset("iris")
# Plotting the KDE Plot 
sns.kdeplot(iris.loc[(iris['species']=='setosa'), 
            'sepal_length'], color='b', shade=True, Label='setosa') 
sns.kdeplot(iris.loc[(iris['species']=='virginica'), 
            'sepal_length'], color='r', shade=True, Label='virginica')
