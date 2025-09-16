import matplotlib.pyplot as plt
import seaborn as sns
  
sns.set_context('paper')
 
# load dataset
titanic = sns.load_dataset('titanic')
# create plot
sns.countplot(x = 'class', hue = 'who', data = titanic, palette = 'magma')
plt.title('Survivors')
plt.show()
