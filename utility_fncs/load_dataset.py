import pandas as pd
import os
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the CSV file by going up one level and then into 'data'
# os.path.join is used to correctly join path components for any OS (Windows, Mac, Linux)
data_dir = os.path.join(script_dir, '..', 'data')

advertising_csv_path = os.path.join(data_dir, 'Advertising.csv')
adv_df=pd.read_csv(advertising_csv_path)
print("DataFrame 'adv_df' for 'Advertising.csv' has been created in the data_loader module.")

credit_card_csv_path = os.path.join(data_dir, 'credit.csv')
credit_df=pd.read_csv(credit_card_csv_path)
print("DataFrame 'credit_df' for 'credit.csv' has been created in the data_loader module.")

poly_csv_path = os.path.join(data_dir, 'poly.csv')
poly_df=pd.read_csv(poly_csv_path)
print("DataFrame 'poly_df' for 'poly.csv' has been created in the data_loader module.")

collinear_csv_path = os.path.join(data_dir, 'colinearity.csv')
collinear_df=pd.read_csv(collinear_csv_path)
print("DataFrame 'collinear_df' for 'colinearity.csv' has been created in the data_loader module.")

dataset_csv_path = os.path.join(data_dir, 'dataset.csv')
dataset_df=pd.read_csv(dataset_csv_path)
print("DataFrame 'dataset_df' for 'dataset.csv' has been created in the data_loader module.")

noisypopulation_csv_path = os.path.join(data_dir, 'noisypopulation.csv')
noisypopulation_df=pd.read_csv(noisypopulation_csv_path)
print("DataFrame 'noisypopulation_df' for 'noisypopulation.csv' has been created in the data_loader module.")

polynomial50_csv_path = os.path.join(data_dir, 'polynomial50.csv')
polynomial50_df=pd.read_csv(polynomial50_csv_path)
print("DataFrame 'polynomial50_df' for 'polynomial50.csv' has been created in the data_loader module.")

insurance_claim_csv_path = os.path.join(data_dir, 'insurance_claim.csv')
insurance_claim_df=pd.read_csv(insurance_claim_csv_path)
print("DataFrame 'insurance_claim_df' for 'insurance_claim.csv' has been created in the data_loader module.")

heart_csv_path = os.path.join(data_dir, 'heart.csv')
heart_df=pd.read_csv(heart_csv_path)
print("DataFrame 'heart_df' for 'heart.csv' has been created in the data_loader module.")