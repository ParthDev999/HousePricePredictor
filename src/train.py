import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# Step 1: Load the dataset
# We read the CSV file because the model learns from this data.
df = pd.read_csv("data/housing.csv")


# Step 2: Separate input features and target
# X contains the house details given to the model.
X = df[["Area", "Bedrooms", "Bathrooms", "Age"]]

# y contains the actual price that the model has to learn.
y = df["Price"]


# Step 3: Split data into training and testing data
# Training data is used to teach the model.
# Testing data is used to check how well the model learned.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Step 4: Create the Linear Regression model
# This model tries to learn a relationship between house details and price.
model = LinearRegression()


# Step 5: Train the model
# fit() means the model is learning patterns from training data.
model.fit(X_train, y_train)


# Step 6: Make predictions on test data
# The model predicts prices for houses it has not seen during training.
predictions = model.predict(X_test)


# Step 7: Evaluate the model
# R2 score tells how well the model performed.
score = r2_score(y_test, predictions)


# Step 8: Save the trained model
# This allows us to reuse the model later without training again.
joblib.dump(model, "models/house_price_model.pkl")


print("Model trained successfully!")
print(f"R2 Score: {score}")
print("Model saved at: models/house_price_model.pkl")