from sklearn.datasets import load_digits as digits
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
import numpy as np
# loading the digits dataset
digits = digits()
x = digits.data
y = digits.target
print("Feature data shape:", x.shape)
print("Target data shape:", y.shape)
print("x input",x[100])
print("y input",[100])

# visualizing some sample digits 
plt.imshow(digits.images[100], cmap='gray')
plt.title(f"Sample Digit: {digits.target[100]}")
plt.axis('off' )
plt.show()

# training test split 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# building the neural network model using ANN pipeline 

model = Pipeline([("scaler", StandardScaler()), ("ann", MLPClassifier(hidden_layer_sizes=(64,), activation='relu', max_iter=500, random_state=42))])
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", round(accuracy, 3))