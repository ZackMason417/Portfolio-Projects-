# Set up filepaths
import os

# Check if file exists, if not, create a symlink
if not os.path.exists(r"C:\\Users\\thety\\Documents\\AutoSort\\CSV Files\\train.csv"):
    os.symlink(r"C:\\Users\\thety\\Documents\\AutoSort\\CSV Files\\train.csv")

# Import necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Define file path for the training data
iowa_file_path = r"C:\\Users\\thety\\Documents\\AutoSort\\CSV Files\\train.csv"

# Read the data into a DataFrame
home_data = pd.read_csv(iowa_file_path)

# Define the target variable
y = home_data.SalePrice

# Define features for the model
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Create the feature matrix (X) using selected features
X = home_data[features]

# Split the data into training and validation sets
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Define a Random Forest Regressor model
rf_model = RandomForestRegressor(random_state=1)

# Train the model on the training data
rf_model.fit(train_X, train_y)

# Make predictions on the validation set
rf_val_predictions = rf_model.predict(val_X)

# Calculate Mean Absolute Error (MAE) to evaluate the model
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

# Print the validation MAE
print("Validation MAE for Random Forest Model:", rf_val_mae)

# Create a new Random Forest model using all training data for improved accuracy
rf_model_on_full_data = RandomForestRegressor(random_state=1)
rf_model_on_full_data.fit(X, y)

# Define file path for the test data
test_data_path = r"C:\\Users\\thety\\Documents\\AutoSort\\CSV Files\\test.csv"

# Read the test data into a DataFrame
test_data = pd.read_csv(test_data_path)

# Select relevant features for prediction from the test data
test_X = test_data[features]

# Make predictions on the test data using the trained model
test_preds = rf_model_on_full_data.predict(test_X)

# Save the predictions to a CSV file for submission
output = pd.DataFrame({'Id': test_data.Id, 'SalePrice': test_preds})
output.to_csv(r"C:\\Users\\thety\\Documents\\AutoSort\\CSV Files\\submission.csv", index=False)
