import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Before creating the model, we have to load the data from the CSV file and pick the most important features for the model

df = pd.read_csv("HR_comma_sep.csv")

# create dummy columns of department and salary, so they can be converted from string to numbers

department_dummies = pd.get_dummies(df["Department"], prefix="Department")
salary_dummies = pd.get_dummies(df["salary"], prefix="Salary")

# We then drop the original department and salary columns since we dont need them anymore, then we add the dummy versions of them

df.drop(["Department", "salary"], axis="columns", inplace=True)
df = pd.concat([df, department_dummies, salary_dummies], axis="columns")

# Then we show the means of the features for each possible outcome (left or remained),
# which would help us visualize and pick the important features

print(df.groupby('left').mean())

# We then make a substitue dataframe with the important features, along with the outcome column

subdf = df[['satisfaction_level','average_montly_hours','promotion_last_5years','Salary_high','Salary_medium','Salary_low']]
y = df["left"]

# Lastly we create our model by first splitting the dataset into train and test,
# and training the model with the train dataset

X_train, X_test, y_train, y_test = train_test_split(subdf, y, test_size=0.3)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
model.predict(X_test)

# This gives the score of our trained model, which gets the answer correct 76%-78% of the time

print(model.score(X_test, y_test))