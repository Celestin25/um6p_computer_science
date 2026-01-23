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
digits_data = digits()
x = digits_data.data
y = digits_data.target

print("Feature data shape:", x.shape)
print("Target data shape:", y.shape)
print("x input:", x[100])
print("y input:", y[100])

# visualizing sample digits same as lab instructions
plt.imshow(digits_data.images[100], cmap='gray')
plt.title(f"Sample Digit: {digits_data.target[100]}")
plt.axis('off')
plt.show()

# training test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# building the neural network model
# using a pipeline to scale and train
model = Pipeline([
    ("scaler", StandardScaler()), 
    ("ann", MLPClassifier(hidden_layer_sizes=(64,), activation='relu', max_iter=500, random_state=42))
])

model.fit(x_train, y_train)

# testing the model
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", round(accuracy, 3))

# predict a new handwritten digit
print("\n--- Predicting a new digit ---")

# picking a sample from test set
sample_idx = 0
new_digit = x_test[sample_idx]
true_label = y_test[sample_idx]

# reshape is needed for predict
new_digit_r = new_digit.reshape(1, -1)

# prediction
pred_label = model.predict(new_digit_r)[0]

print(f"Index: {sample_idx}")
print(f"True Label: {true_label}")
print(f"Predicted: {pred_label}")

# showing the image
plt.figure()
plt.imshow(new_digit.reshape(8, 8), cmap='gray')
plt.title(f"True: {true_label} | Pred: {pred_label}")
plt.axis('off')
plt.show()