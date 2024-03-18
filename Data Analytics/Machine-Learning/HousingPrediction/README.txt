# PY-HousingML

Welcome to the PY-HousingML project! This project is inspired by the book "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" by Aurélien Géron. It involves predicting housing prices using Python and various machine learning algorithms.

## Overview

This repository contains a collection of Python scripts for fetching, analyzing, and modeling housing data. The project focuses on using machine learning techniques to predict housing prices based on various features such as median income, location, and housing characteristics.

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

5. **Feature Engineering**
   - Calculates additional features such as rooms per household and bedrooms per room.
   - Handles missing values using `SimpleImputer`.

6. **Machine Learning Models**
   - Implements various regression models:
     - Linear Regression
     - Decision Tree Regression
     - Random Forest Regression

7. **Model Evaluation**
   - Uses cross-validation to evaluate model performance.
   - Calculates root mean squared error (RMSE) for model evaluation.

## Techniques Used
- Data fetching with `urllib` and `tarfile`.
- Data manipulation and analysis with `pandas`.
- Exploratory Data Analysis (EDA) using descriptive statistics and visualization.
- Feature engineering to create new attributes for analysis.
- Train-Test Split using custom functions.
- Implementation and evaluation of machine learning regression models.

Project Outcome
Successful fetching and loading of the housing dataset.
Clear understanding of the dataset's structure and attributes.
Creation of training and testing sets for model development.
Implementation and evaluation of machine learning models.
Model predictions and evaluation metrics displayed in the terminal.

Dependencies
Python 3.x
NumPy
pandas
matplotlib
scikit-learn
joblib
Author
Zack Mason
