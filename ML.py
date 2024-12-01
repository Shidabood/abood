import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

# Here i load the data from the csv file, clean it,
# And set the X as the duration of the gym session and Y is the calories burnt

df = pd.read_csv('data.csv')

df["Calories"].fillna(df["Calories"].mode()[0], inplace=True)
df.drop_duplicates(inplace=True)

X_duration = df[['Duration']]
Y_calories = df['Calories']

# And here i initialize the linear regression model from scikit learn

model = LinearRegression()

model.fit(X_duration, Y_calories)

w = model.coef_[0]  # Slope
b = model.intercept_  # Intercept

y_pred = model.predict(X_duration)

print(f"Slope (w): {w:.5f}, Intercept (b): {b:.5f}")

# Plot the data set and its regression line (the line that minimizes the loss function)

plt.scatter(X_duration, Y_calories, color='blue', label='Data points')
plt.plot(X_duration, y_pred, color='red', label='Regression line')
plt.title('Predicted value of calories based on the duration')
plt.xlabel('Duration')
plt.ylabel('Calories burnt')
plt.legend()
plt.show()