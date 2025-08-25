# Task4
# Nancy Lampropoulou

# This program retrieves employee data from a web service, cleans the data by handling missing values,
# calculates total salary (salary + bonus), generates descriptive statistics,
# filters and displays high-paid employees in the Marketing department,
# and creates visual plots of the number of employees per department and high-paid Marketing employees.


import pandas as pd
import json
import requests
from pandas import json_normalize
import matplotlib.pyplot as plt


# Call the webservice
response = "https://my.api.mockaroo.com/company_data.json?key=fdad79b0"
results = requests.get(response).json()

# Use json_normalize() to convert JSON to DataFrame
df = json_normalize(results)

# Preview data frame
print(df.head(10))

# Update missing values for numeric fields to 0 using fillna function
df[["salary","bonus"]] = df[["salary","bonus"]].fillna(0)

# preview the DataFrame to check the changes
print(df.head(10))

# Update missing values for character fields to 'NA'
col_list = ['id', 'first_name', 'last_name', 'email', 'gender', 'department', 'dateOfBirth']
nan_replaced = ['id_edited', 'first_name_edited', 'last_name_edited', 'email_edited', 'gender_edited', 'department_edited', 'dateOfBirth_edited']
# Create the new columns (nan_replaced) by copying the corresponding ones from col_list
df[nan_replaced] = df[col_list]
# use fillna() to replace missing values with 'NA' in the new columns
df[nan_replaced] = df[col_list].fillna('NA')


# Create new column: TotalSalary = Salary + Bonus calculated by adding 'salary' and 'bonus' for each row.
df['TotalSalary'] = df['salary'] + df['bonus']

# Descriptive Statistics shows a summary of numeric columns like mean, min, max, and standard deviation.
print("\nDescriptive Statistics:")
print(df.describe())

# How many rows exists in the 'department' field
department_counts = df['department'].value_counts()

# Print the counts
print("Department counts:")
print(department_counts)

# A meaningful subset of the data to focus on high-paid employees in the 'Marketing' department
# Subset: Only employees in the 'Marketing' department with a TotalSalary > 5000
df_highly_paid_marketing_employees = df[(df['department'] == 'Marketing') & (df['TotalSalary'] > 5000)]

# Purpose: To identify high-earning employees in the Marketing department.
print("\nEmployees with Highest Salary in Marketing Department:")
print(df_highly_paid_marketing_employees)

# Plot 1: Shows the number of employees in each department. This helps the user understand
# which departments have the most employees and which have fewer employees.
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x=department_counts.index, height=department_counts.values, color="purple")
ax.set(title="Employees by Department", xlabel="Department", ylabel="Number of Employees")
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout for better spacing
plt.savefig('department_count_bar_chart.png')  # Save the plot as an image file




# Plot 2: Highly Paid Employees in the 'Marketing' Department, this gives visual to the user who are these employees
# Using 'first_name' as x-axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x=df_highly_paid_marketing_employees['first_name'], height=df_highly_paid_marketing_employees['TotalSalary'], color="green")
ax.set(title="Highly Paid Marketing Employees", xlabel="Employee Name", ylabel="Total Salary")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('highly_paid_employees.png')  # Save the plot as an image file

