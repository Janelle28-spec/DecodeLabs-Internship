# ==========================================================
# DECODELABS AI PROJECT 2
# DATA CLASSIFICATION USING AI (Iris flowers, KNN)
# ==========================================================

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# ----------------------------------------------------------
# STEP 1: LOAD AND UNDERSTAND THE DATASET
# ----------------------------------------------------------
iris = load_iris()

# Put the data in a table so it is easy to read
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data["species"] = [iris.target_names[i] for i in iris.target]

print("First 5 rows:")
print(data.head())
print("\nShape (rows, columns):", data.shape)
print("\nSamples per species:")
print(data["species"].value_counts())

# ----------------------------------------------------------
# STEP 2: SPLIT INTO TRAINING AND TESTING SETS
# ----------------------------------------------------------
X = iris.data      # features (measurements)
y = iris.target    # labels (species 0, 1, 2)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining samples:", len(X_train))
print("Testing samples: ", len(X_test))

# ----------------------------------------------------------
# STEP 3: TRAIN A CLASSIFICATION MODEL (K-Nearest Neighbors)
# ----------------------------------------------------------
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# ----------------------------------------------------------
# STEP 4: TEST THE MODEL
# ----------------------------------------------------------
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"\nModel accuracy: {accuracy * 100:.1f}%")
print("\nConfusion matrix (rows = actual, columns = predicted):")
print(confusion_matrix(y_test, predictions))

# ----------------------------------------------------------
# # STEP 5: PREDICT NEW FLOWERS
new_flowers = [
    [5.1, 3.5, 1.4, 0.2],
    [6.0, 2.9, 4.5, 1.5],
    [6.5, 3.0, 5.8, 2.2],
]
for flower in new_flowers:
    result = model.predict([flower])
    print("Flower", flower, "is predicted to be:", iris.target_names[result[0]])