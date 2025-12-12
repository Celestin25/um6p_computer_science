# importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# creating numpy arrays
x_array = np.array([1, 2, 3, 4, 5, 6])
y_array = np.array([52, 58, 66, 71, 82, 94])
# displaying shape of arrays
print(x_array.shape)
print(y_array.shape)
# visualizing data using line plot and scatter plot
plt.plot(x_array, y_array, color='red', marker='o', linestyle='--')
plt.scatter(x_array, y_array, color='blue', marker='D')
plt.title("Scatter Plot of X vs Y")
# showing the plot
# plt.show()
# training the linear regression model using numpy
split_index = 4
x_train = x_array[:split_index]
x_test = x_array[split_index:]
y_train = y_array[:split_index]
y_test = y_array[split_index:]

print("x_train", x_train)
print("x_test", x_test)
print("y_train", y_train)
print("y_test", y_test)

x_array_mean = np.mean(x_array)
y_array_mean = np.mean(y_array)

n = len(x_train)
m = (n * np.sum(x_train * y_train) - np.sum(x_train) * np.sum(y_train)) / \
    (n * np.sum(x_train ** 2))-(np.sum(x_train)**2)
b = (np.sum(y_train)-m*np.sum(x_train)) / n
print("slope:", m)
print("intercept:", b)

# Evaluating on test only
y_pred = m * x_test + b
print("Predicted values:", y_pred)
# comparing actual vs predicted
print("x_test:", x_test)
print("actual y_test:", y_test)
print("predicted y_test:", y_pred)
# evaluating performance
mse = np.mean((y_test - y_pred) ** 2)
print("Mean Squared Error:", round(mse, 2))

# predict for a new hours after training

new_x = np.array([7])
new_y = m * new_x + b
print("Predicted value for new_x (7):", new_y)
# plotting the train fit line with both train/test points
plt.plot(x_train, m * x_train + b, color='green', label='Train Fit Line')
plt.scatter(x_train, y_train, color='blue', label='Train Data', marker='o')
plt.scatter(x_test, y_test, color='orange', label='Test Data', marker='x')
plt.title("Train Fit Line with Train and Test Data")
plt.legend()
plt.show()
