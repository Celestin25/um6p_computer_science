from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split       
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import numpy as np 
iris =load_iris() 
x = iris['data']
y = iris['target']
plt.scatter(x[:, 0], x[:, 2], c=y, cmap='viridis')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title("Iris Dataset(colored by species)")

cbar=plt.colorbar()
cbar.set_label('Species')
cbar.set_ticks([0,1,2])
cbar.set_ticklabels(['Setosa', 'Versicolor', 'Virginica'])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

model = Pipeline([
    ("scaler", StandardScaler()),
    ("svm", SVC(kernel="rbf", C=1, gamma='scale')) 
])                                      
model.fit(xtrain, ytrain)
y_pred = model.predict(xtest)
acc= model.score(xtest, ytest)
print(f"Model Accuracy: {acc:.3f}%")
new_sample= np.array([[5.1, 3.5, 1.4, 0.2]])
new_pred = model.predict(new_sample)[0]
label_map = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
print("New Sample Prediction:", label_map[new_pred])
