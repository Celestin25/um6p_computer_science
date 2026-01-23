import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline

# Part A: Breast Cancer Dataset - KNN vs SVM

# 1. Import Dataset
data = load_breast_cancer()
X = data.data
y = data.target
print(f"Dataset shape: {X.shape}")

# 2. Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")

# 3. Pipelines
# KNN
knn_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5))
])

# SVM
svm_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(kernel='rbf', C=1.0, random_state=42))
])

# 4. Fit and Evaluate
print("\n--- Breast Cancer Results ---")
models = [("KNN", knn_pipe), ("SVM", svm_pipe)]

for name, model in models:
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"{name} Accuracy: {acc:.4f}")
    
    # Predict for a new point (using the first test point as example)
    new_point = X_test[0].reshape(1, -1)
    prediction = model.predict(new_point)[0]
    print(f"Prediction for new point ({name}): {prediction}")


# Part B: Students Performance Dataset

print("\n--- Student Performance Results ---")

# loading the csv file
# make sure student_performance.csv is in the same folder
df = pd.read_csv("student_performance.csv")
print("Student data loaded.")

# using GradeClass as the target
target_col = 'GradeClass' 

# dropping columns we don't need for training
drop_cols = ['StudentID', 'GPA', 'GradeClass']

# selecting features
# getting all columns except the dropped ones
feature_cols = [c for c in df.columns if c not in drop_cols]

X_student = df[feature_cols]
y_student = df[target_col]

# split data
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_student, y_student, test_size=0.2, random_state=42, stratify=y_student)

# training and checking accuracy
knn_s = Pipeline([('scaler', StandardScaler()), ('knn', KNeighborsClassifier(n_neighbors=5))])
svm_s = Pipeline([('scaler', StandardScaler()), ('svm', SVC(kernel='rbf', random_state=42))])

for name, model in [("KNN", knn_s), ("SVM", svm_s)]:
    model.fit(X_train_s, y_train_s)
    acc = model.score(X_test_s, y_test_s)
    print(f"{name} Student Accuracy: {acc:.4f}")
    
# prediction example
sample_student = X_test_s.iloc[0].values.reshape(1, -1)
pred_knn = knn_s.predict(sample_student)[0]
print(f"KNN Prediction for student: {pred_knn}")


# Part C: Hyperparameters

print("\n--- Hyperparameters Experiment ---")

# 1. Changing N neighbors
k_list = [3, 7, 15]
for k in k_list:
    # reusing the breast cancer data
    model = Pipeline([('scaler', StandardScaler()), ('knn', KNeighborsClassifier(n_neighbors=k))])
    model.fit(X_train, y_train)
    print(f"KNN (k={k}) Accuracy: {model.score(X_test, y_test):.4f}")

# 2. Changing SVM Kernels
kernels = ['linear', 'rbf', 'poly']
for k in kernels:
    model = Pipeline([('scaler', StandardScaler()), ('svm', SVC(kernel=k, random_state=42))])
    model.fit(X_train, y_train)
    print(f"SVM (kernel={k}) Accuracy: {model.score(X_test, y_test):.4f}")

# 3. Classification Report for best KNN
print("\n--- Final Report (KNN k=7) ---")
best_knn = Pipeline([('scaler', StandardScaler()), ('knn', KNeighborsClassifier(n_neighbors=7))])
best_knn.fit(X_train, y_train)
y_pred_final = best_knn.predict(X_test)

print(classification_report(y_test, y_pred_final))
