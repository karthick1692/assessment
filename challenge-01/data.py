import pandas as pd

# Load Excel file with two sheets: Employees and Devices
file_path = './table_data.xlsx'  # replace with the actual file path

# Read the sheets into DataFrames
employees_df = pd.read_excel(file_path, sheet_name='Employees')
devices_df = pd.read_excel(file_path, sheet_name='Devices')

# Perform a left merge to find employees without devices
merged_df = pd.merge(employees_df, devices_df, left_on='id', right_on='employee_id', how='left', indicator=True)

# Filter the merged DataFrame to find employees without a device record
employees_without_devices = merged_df[merged_df['_merge'] == 'left_only']

# Output the first name and last name of employees without devices
print(employees_without_devices[['first_name', 'last_name']])
