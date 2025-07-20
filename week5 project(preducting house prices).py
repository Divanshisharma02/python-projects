import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Day 30: Line, Bar, Pie Charts using Matplotlib

# Line Chart
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.savefig("line_chart.png")

# Bar Chart
categories = ['A', 'B', 'C']
values = [10, 15, 7]
plt.figure()
plt.bar(categories, values, color='skyblue')
plt.title("Bar Chart")
plt.savefig("bar_chart.png")

# Pie Chart
sizes = [40, 35, 25]
labels = ['Python', 'Java', 'C++']
plt.figure()
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.savefig("pie_chart.png")

# Day 31: Seaborn - Histogram, Boxplot, Heatmap

# Load Iris dataset
iris = sns.load_dataset("iris")

# Histogram
plt.figure()
sns.histplot(iris["sepal_length"], kde=True)
plt.title("Histogram of Sepal Length")
plt.savefig("histogram.png")

# Boxplot
plt.figure()
sns.boxplot(x="species", y="sepal_length", data=iris)
plt.title("Boxplot of Sepal Length by Species")
plt.savefig("boxplot.png")

# Heatmap
plt.figure()
sns.heatmap(iris.corr(), annot=True, cmap="coolwarm")
plt.title("Heatmap of Iris Dataset")
plt.savefig("heatmap.png")

# Day 32: Real-World Dataset Exploration - Iris
# Display basic info and head
print("Iris Dataset Info:")
print(iris.info())
print("\nFirst 5 rows:")
print(iris.head())

# Day 33: Intro to Machine Learning Concepts
print("\nMachine Learning Concepts:")
print(" - Supervised vs Unsupervised Learning")
print(" - Features and Labels")
print(" - Training and Testing Data")

# Day 34: Simple Linear Regression using Scikit-learn

# Using petal length to predict petal width
X = iris[["petal_length"]]
y = iris["petal_width"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\nModel Coefficients:")
print(f"Intercept: {model.intercept_}, Coefficient: {model.coef_[0]}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")
print(f"R^2 Score: {r2_score(y_test, y_pred):.2f}")

# Plotting regression
plt.figure()
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.title("Linear Regression: Petal Length vs Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.savefig("regression_plot.png")
