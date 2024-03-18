# PY-HousingML

Welcome to the PY-HousingML project! This project is inspired by the book "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" by Aurélien Géron. It involves predicting housing prices using Python and various machine learning algorithms.

## Project Structure

1. **Fetch Housing Data**
   - Downloads the dataset from an online source.
   - Utilizes `urllib` and `tarfile` for handling data download and extraction.

2. **Load Housing Data**
   - Loads the housing dataset into a pandas DataFrame.

3. **Exploratory Data Analysis (EDA)**
   - Displays the first few rows of the dataset to understand its structure.
   - Provides a summary of the dataset including columns, data types, and non-null counts.
   - Displays the distribution of values in the 'ocean_proximity' column.
   - Generates descriptive statistics of the numerical columns in the dataset.
   - Visualizes histograms of the numerical attributes in the dataset.

4. **Train-Test Split**
   - Splits the dataset into training and testing sets.

5. **Additional Functions**
   - Functions for splitting the data based on an identifier.

## Techniques Used
- Data fetching with `urllib` and `tarfile`.
- Data manipulation and analysis with `pandas`.
- Exploratory Data Analysis (EDA) using descriptive statistics and visualization.
- Train-Test Split using custom functions.
- Machine learning algorithms: Linear Regression, Decision Tree, Random Forest.

## Challenges Faced
- Ensuring the dataset is correctly downloaded and extracted.
- Handling missing values in the dataset during analysis.
- Creating a reliable train-test split for machine learning model evaluation.

## Outcomes
- Successful fetching and loading of the housing dataset.
- Clear understanding of the dataset's structure and attributes.
- Creation of training and testing sets for future model development.
- Implementation and evaluation of machine learning models for housing price prediction.

## Usage
1. Clone the repository:
   git clone https://github.com/your_username/PY-HousingML.git
Navigate to the project directory:

cd PY-HousingML
Run the housing_ml.py script:

python housing_ml.py
Dependencies
Python 3.x
NumPy
pandas
matplotlib
scikit-learn
joblib
Author
Zack Mason
