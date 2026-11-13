# Iris Flower Classifier

## Description
A supervised machine learning project built in Python for the DecodeLabs AI internship. It loads the classic Iris dataset (150 flowers, 3 species), splits it into training and testing sets, trains a K-Nearest Neighbors classifier, and evaluates how accurately it predicts flower species. It then classifies new, unseen flowers.

## What It Does
1. Loads and explores the Iris dataset with pandas
2. Splits the data: 80% training (120 samples), 20% testing (30 samples)
3. Trains a K-Nearest Neighbors model (`n_neighbors=3`)
4. Evaluates the model with accuracy and a confusion matrix
5. Predicts the species of new flowers from their measurements

## Results
- Test accuracy: **100%** (30 of 30 test flowers classified correctly, `random_state=42`)
- New flower predictions:
  - `[5.1, 3.5, 1.4, 0.2]` is predicted to be setosa
  - `[6.0, 2.9, 4.5, 1.5]` is predicted to be versicolor
  - `[6.5, 3.0, 5.8, 2.2]` is predicted to be virginica

## Technologies
- Python 3
- pandas
- scikit-learn

## How to Run
Install the required libraries:
```
pip install scikit-learn pandas
```

Run the program:
```
python classifier.py
```

## Key Learning
A model must be tested on data it has never seen. Splitting the data into training and testing sets shows whether the model learned real patterns instead of memorizing examples.