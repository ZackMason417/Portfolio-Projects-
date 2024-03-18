# Kaggle Housing Prices Machine Learning

Kaggle machine learning project focused on predicting housing prices. The project was submitted to a Kaggle competition and involves feature engineering and model training. This Python project is developed based on the comprehensive Kaggle course "Intro to Machine Learning." The course is available [here](https://www.kaggle.com/learn/intro-to-machine-learning).

## Project Structure

1. **Set up filepaths**
   - Sets up filepaths for data loading and saving.

2. **Random Forest Model**
   - Imports necessary libraries such as pandas and scikit-learn.
   - Loads the housing dataset into a pandas DataFrame.
   - Defines features for the model.
   - Splits the dataset into training and validation sets.
   - Trains a Random Forest Regressor model on the training data.
   - Evaluates the model's performance on the validation set.

3. **Generate Predictions**
   - Creates a new Random Forest model using all training data.
   - Reads test data from a CSV file.
   - Selects relevant features for prediction.
   - Makes predictions on the test data using the trained model.
   - Saves the predictions to a CSV file for submission.

## Usage

1. Clone the repository:
git clone https://github.com/your_username/Kaggle-Housing-ML.git

Navigate to the project directory:
cd Kaggle-Housing-ML


2. Run the Jupyter notebook:
jupyter notebook

Open and run the `Kaggle_Housing_Prices.ipynb` notebook to see the project code and results.

## Dependencies
- Python 3.x
- pandas
- scikit-learn

## Kaggle Competition
- This project was developed for the [Kaggle Housing Prices competition](https://www.kaggle.com/c/house-prices-advanced-regression-techniques).

## Credits
- Project based on the "Intro to Machine Learning" course on Kaggle.
- Author: Zack Mason
