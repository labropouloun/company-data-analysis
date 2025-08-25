\# Company Data Analysis



Final Program: Processing of a Company's Employee Data



\## Project General Information



This program is made up to process and analyze employee information of a company. The aim is to use data files to perform tasks like sorting, statistics, searching, filtering, and showing visuals. It supports CSV and JSON formats for ease and makes sure the data is cleaned well. By combining these tasks, the program provides meaningful insights into the employee dataset, help the user to explore and understand the data effectively.

The dataset (100 rows) was generated with \[Mockaroo](https://mockaroo.com/) and contains the following columns:



1. 'id': A unique identifier for each employee.
2. 'first\_name: The employee's first name.
3. 'last\_name': The employee's last name.
4. 'email': The employee's email address.
5. 'gender': The gender of the employee.
6. 'department': The department in which the employee works.
7. 'salary': The salary of the employee.
8. 'bonus': Additional bonus received by the employee.
9. 'dateOfBirth': The employee's date of birth.



The program is split into four tasks, with each one focused on a different piece of data handling and analysis.



\## Project Structure



company-data-analysis/

-- CompanyData.csv

-- README.md

-- company_data.json

-- companydata_analysis.py # main program

-- requirements.txt

-- task1.py

-- task2.py

-- task3.py

-- task4.py


\## Installation


Clone the repository:


git clone https://github.com/labropouloun/company-data-analysis.git

cd company-data-analysis

pip install -r requirements.txt



\# Run the main program:



python companydata\_analysis.py



\# Run individual tasks:



python task1.py

python task2.py

python task3.py

python task4.py



\## Libraries Used



pandas

requests

matplotlib



\## Author

Nancy Labropoulou

GitHub: labropouloun



\## Task Descriptions



\# Task 1 Files, Input/Output, String/Number Manipulation, Lists:



This task focuses on importing and processing the dataset:

* Reads the employee data from a CSV file.
* Mixes the first and last names into one spot (whole name).
* Sorts the employee data alphabetically by whole name.
* Checks user input to make sure only the ͏asked number of rows is shown.
* Outputs the processed formatted data.



\# Task 2 Reading CSV Files, Lists, Sets, Dictionaries and Manipulating Data:



This task analyzes the department field and calculates statistics:

* Processes the employee data and organizes it into a list of dictionaries.
* It gives information of the number of employees for each department and of the company's total salaries, average salary, and total number of employee's.
* Checks user answer for the count of rows to show when displaying results.
* Displays the data in a formatted output.



\# Task 3 Object-oriented programming (OOP), JSON:



This task is managing data from a JSON file:

* Defines an object, with all the instance attributes included in the JSON file.
* Displays all available employee information formatted.
* Searches for employees by specific attributes such as 'department', 'first\_name', or 'gender'.
* Filters employees based on numeric attribute, salaries, bonus and id beyond the user entered value.
* Prints the result's formatted.



\# Task 4 Web Services, Pandas, MatPlotlib:



This task not only uses Pandas to create a DataFrame, but also perform basic DataFrame manipulation :

* Retrieves employees data from a web service and imports it into the program.
* Cleans the data by handling missing values in numeric and character fields.
* Computes the total salary ('salary' + 'bonus') for all employees.
* Filters and identifies high-paid employees in the Marketing department.
* Generates descriptive statistics, providing a summary of numeric data fields such as 'salary' and 'bonus'.
* Creates visualizations to represent data trends:

  * A bar chart showing the number of employees in each department.
  * A bar chart highlighting high-paid employees in the Marketing department.
