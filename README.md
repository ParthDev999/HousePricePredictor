# 🏠 House Price Predictor

A Machine Learning web application that predicts house prices based on property features such as area, number of bedrooms, bathrooms, and house age.

The project uses a Linear Regression model trained on housing data and provides real-time predictions through an interactive Streamlit web interface.

---

## 🚀 Features

- Predict house prices using Machine Learning
- Interactive web interface built with Streamlit
- Data visualization using Matplotlib
- Model training using Scikit-Learn
- Model evaluation using R² Score
- Save and load trained models using Joblib

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Joblib
- Streamlit

---

## 📂 Project Structure

```text
HousePricePredictor/
│
├── data/
│   └── housing.csv
│
├── models/
│   └── house_price_model.pkl
│
├── src/
│   ├── train.py
│   ├── predict.py
│   └── visualize.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📊 Machine Learning Workflow

```text
Dataset
   ↓
Data Preprocessing
   ↓
Train/Test Split
   ↓
Linear Regression Model
   ↓
Model Evaluation (R² Score)
   ↓
Model Saving (.pkl)
   ↓
Streamlit Web Application
```

---

## 📈 Model Performance

The model was evaluated using the R² Score metric.

```text
R² Score ≈ 0.997
```

This indicates that the model explains approximately 99.7% of the variation in house prices for the given dataset.

---

## 🏡 Input Features

The model predicts house prices using:

| Feature | Description |
|----------|------------|
| Area | Area of the house in square feet |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Age | Age of the house in years |

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ParthDev999/HousePricePredictor.git
```

Move into the project directory:

```bash
cd HousePricePredictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

```bash
python src/train.py
```

This will:

- Load the dataset
- Train the Linear Regression model
- Evaluate performance
- Save the trained model

---

## 🌐 Run the Web App

```bash
streamlit run app.py
```

Then open the URL displayed in the terminal.

---

## 📷 Sample Prediction

Example Input:

```text
Area: 2100 sq ft
Bedrooms: 3
Bathrooms: 3
Age: 4 years
```

Example Output:

```text
Predicted House Price: ₹8,500,000
```

---

## 🎯 Future Improvements

- Larger real-world housing dataset
- Advanced regression models
  - Decision Tree Regressor
  - Random Forest Regressor
  - XGBoost
- Better feature engineering
- Cloud deployment
- Improved UI and visualization

---

## 👨‍💻 Author

**Parth Sawaria**

GitHub: https://github.com/ParthDev999

---

⭐ If you found this project useful, consider giving it a star.
