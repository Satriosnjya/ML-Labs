# -*- coding: utf-8 -*-
"""Labs2_Classification_Student.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WL5mIX1ZnY75Law2BJQx8DznMNp5m78B
"""



"""Dataset Explanation"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
file_path = "classification.csv"
df = pd.read_csv(file_path)

# Display dataset information and preview
df_info = df.info()

df.head()

"""**Dataset Explanation**

This dataset appears to be a binary classification dataset where the goal is to predict a categorical outcome (y) based on various demographic and economic factors.

**Dataset Structure**
1. Number of Rows: 48,842
2. Number of Columns: 11
3. Target Variable: y (Binary: 0 or 1)
4. Feature Variables (Categorical):
* hours_per_week_bin: Categorized work hours per week.
* occupation_bin: Grouped occupation levels.
* msr_bin: Economic or marital status classification.
* capital_gl_bin: Categorized capital gain/loss.
* race_sex_bin: Combined race and gender category.
* education_num_bin: Grouped education years.
* education_bin: Education level classification.
* workclass_bin: Type of work category.
* age_bin: Age grouped into bins.
* flag: Indicates training (train) or test (test) set.

Classification Tasks: The goal of the classification model (Logistic/Probit Regression) is to predict y, which is a binary label (0 or 1). What are we classifying? We are predicting whether an individual earns more than 50K per year based on demographic and work-related factors.

Data preparation
"""

# Data Preparation
cat_feats = ['age_bin','capital_gl_bin','education_bin','hours_per_week_bin','msr_bin','occupation_bin','race_sex_bin']

# Split dataset into train and test
y_train = df[df['flag']=='train']['y']
x_train = df[df['flag']=='train'][cat_feats]
x_train = pd.get_dummies(x_train, columns=cat_feats, drop_first=True)

y_test = df[df['flag']=='test']['y']
x_test = df[df['flag']=='test'][cat_feats]
x_test = pd.get_dummies(x_test, columns=cat_feats, drop_first=True)

# Convert to numpy arrays
x_train, y_train = x_train.values, y_train.values
x_test, y_test = x_test.values, y_test.values

# Apply manual feature scaling
mean_train = np.mean(x_train, axis=0)
std_train = np.std(x_train, axis=0)
x_train_scaled = (x_train - mean_train) / std_train
x_test_scaled = (x_test - mean_train) / std_train

"""Assignment"""

# Logistic Regression from Scratch
class LogisticRegressionScratch:
    def __init__(self, learning_rate=0.01, iterations=3000):
        pass

    def fit(self, X, y):
        pass

    def predict_proba(self, X):
        pass

    def predict(self, X, threshold=0.5):
        pass

# Probit Regression from Scratch
class ProbitRegressionScratch:
    def __init__(self, learning_rate=0.01, iterations=3000):
        pass

    def fit(self, X, y):
        pass

    def predict_proba(self, X):
        pass

    def predict(self, X, threshold=0.5):
        pass

# Train Models
lr_scratch = LogisticRegressionScratch()
lr_scratch.fit(x_train, y_train)

pr_scratch = ProbitRegressionScratch()
pr_scratch.fit(x_train, y_train)

# Predictions
y_pred_lr = lr_scratch.predict(x_test)
y_prob_lr = lr_scratch.predict_proba(x_test)

y_pred_pr = pr_scratch.predict(x_test)
y_prob_pr = pr_scratch.predict_proba(x_test)

# Compute Confusion Matrices
def compute_confusion_matrix(y_true, y_pred):
    pass

cm_lr = compute_confusion_matrix(y_test, y_pred_lr)
cm_pr = compute_confusion_matrix(y_test, y_pred_pr)

# Compute ROC Curves and AUC
def compute_roc_curve(y_true, y_scores):
    pass

def compute_auc(fpr, tpr):
    pass

#fpr_lr, tpr_lr = compute_roc_curve(y_test, y_prob_lr)
#fpr_pr, tpr_pr = compute_roc_curve(y_test, y_prob_pr)
#auc_lr = compute_auc(fpr_lr, tpr_lr)
#auc_pr = compute_auc(fpr_pr, tpr_pr)

