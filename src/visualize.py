import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/housing.csv")

# Area vs Price
plt.figure(figsize=(8,5))
plt.scatter(df["Area"], df["Price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()

# Bedrooms vs Price
plt.figure(figsize=(8,5))
plt.scatter(df["Bedrooms"], df["Price"])
plt.xlabel("Bedrooms")
plt.ylabel("Price")
plt.title("Bedrooms vs Price")
plt.show()

# Bathrooms vs Price
plt.figure(figsize=(8,5))
plt.scatter(df["Bathrooms"], df["Price"])
plt.xlabel("Bathrooms")
plt.ylabel("Price")
plt.title("Bathrooms vs Price")
plt.show()

# Age vs Price
plt.figure(figsize=(8,5))
plt.scatter(df["Age"], df["Price"])
plt.xlabel("Age")
plt.ylabel("Price")
plt.title("Age vs Price")
plt.show() 