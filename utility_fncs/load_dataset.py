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