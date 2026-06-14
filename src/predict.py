import joblib


# Step 1: Load the trained model
model = joblib.load("models/house_price_model.pkl")


try:
    # Step 2: Take user input
    area = float(input("Enter Area in sq ft: "))
    bedrooms = int(input("Enter Number of Bedrooms: "))
    bathrooms = int(input("Enter Number of Bathrooms: "))
    age = int(input("Enter Age of House in years: "))

    # Step 3: Basic validation
    if area <= 0 or bedrooms <= 0 or bathrooms <= 0 or age < 0:
        print("Invalid input. Please enter positive values.")
    else:
        # Step 4: Prepare data for prediction
        new_house = [[area, bedrooms, bathrooms, age]]

        # Step 5: Predict price
        predicted_price = model.predict(new_house)

        # Step 6: Display clean output
        print("\nPrediction Result")
        print("-----------------")
        print(f"Area: {area} sq ft")
        print(f"Bedrooms: {bedrooms}")
        print(f"Bathrooms: {bathrooms}")
        print(f"Age: {age} years")
        print(f"Predicted House Price: ₹{predicted_price[0]:,.0f}")

except ValueError:
    print("Invalid input. Please enter numbers only.")