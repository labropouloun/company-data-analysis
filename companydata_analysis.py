def read_csv_to_list(filename):

    # Reads a CSV file line by line (ignores headers) and returns a list of lists.
    # Combines 'first_name' and 'last_name' into a single 'first_name and last_name' field.

    data = []  # Initialize an empty list to store the processed data rows
    # Open the file in read mode
    with open(filename, 'r') as file:
        lines = list(file)  # Read all lines from the file into a list
        for line in lines[1:]:  # Skip the first line (header) using index-based slicing
            row = line.strip().split(',')  # Remove any whitespace and split the line by commas
            full_name = f"{row[1]} {row[2]}"  # Combine 'first_name' and 'last_name' into a single string
            row[1] = full_name  # Replace the 'first_name' column with the combined 'Full Name'
            del row[2]  # Remove the 'last_name' column
            data.append(row)  # Append the modified row to the 'data' list
    return data  # Return the processed list of data rows


def sort_by_name(data):
    # Sorts a list of lists by full name.

    # Arguments: data as List of lists to be sorted.

    # Returns: A sorted list of lists containing simplified fields:
    # [['Full Name', 'Department', 'Salary', 'Bonus', 'Gender']]

    simplified_data = []  # Initialize an empty list to store simplified rows
    for row in data:  # Iterate over each row in the input data
        # Create a simplified row containing selected fields:
        # [Full Name, Department, Salary, Bonus, Gender]
        simplified_row = [row[1], row[4], row[5], row[6], row[3]]
        simplified_data.append(simplified_row)  # Add the simplified row to the new list

    # Sort the list of simplified rows by Full Name
    simplified_data.sort()

    return simplified_data  # Return the sorted list of simplified data



def validate_row_input():

    # Prompts the user to input a number of rows to display (0-100) and ensures the input is valid

    while True:  # Begin an infinite loop to continuously prompt the user until valid input is provided
        try:
            # Prompt the user to input a number of rows and attempt to convert it to an integer
            rows = int(input("How many rows do you want to display? "))
            # Check if the input number is within the valid range (0-100)
            if rows >= 0 and rows <= 100:
                return rows  # Return the valid input and exit the loop
            else:
                # Inform the user that the input must be within the specified range
                print("Error: Please enter a number between 0 and 100.")
        except:
            # Handle invalid input (e.g., non-integer values) and prompt the user again
            print("Error: Invalid input. Please enter a valid integer.")



def format_data(data, number_rows):

    # Formats and displays the data, showing only the specified number of rows.

    # Arguments: data: List of lists containing the data to be formatted, and number_rows: The number of rows to display.

    # Print the formatted header
    print("-" * 60)

    # Display the formatted rows
    for i in range(len(data)):  # Loop through the data list by index
        if i >= number_rows:  # Stop printing rows if the specified limit is reached
            break  # Exit the loop if the number of displayed rows equals the limit

        row = data[i]  # Access the current row of data
        # Extract the specific fields from the row for readability
        name, department, salary, bonus, gender = row

        # Print the row in a formatted style using f-strings:
        # - `<20` aligns 'name' to the left with a width of 20 characters
        # - `<15` aligns 'department' to the left with a width of 15 characters
        # - `>5` aligns 'salary' to the right with a width of 5 characters
        # - `>10` aligns 'bonus' to the right with a width of 10 characters
        # - `>10` aligns 'gender' to the right with a width of 10 characters
        print(f"{name:<20} {department:<15} {salary:>5} {bonus:>10} {gender:>10}")



# TASK 2 Functions-----------
import csv

def read_csv_file(file_path):
    # List to store the dictionaries
    data = []

    # Open the CSV file in read mode ('r') using the 'with' statement
    with open(file_path, 'r') as file:
        # Create a CSV reader object
        # The csv.DictReader() reads each row as an ordered dictionary where the keys are the column headers
        csv_reader = csv.DictReader(file)

        # Iterate through the rows in the CSV file and append each to the list
        for row in csv_reader:
            data.append(row) # Adds each dictionary (representing a row) to the 'data' list

    return data # Returns the 'data' list, which contains all rows from the CSV file as dictionaries


def count_employees_per_department(file_path):
    # Dictionary to store the count of employees per department
    # This dictionary will have department names as keys and the number of employees in each department as values
    count_department = {} # Initialize an empty dictionary to keep track of department counts

    # Read the CSV data
    data = read_csv_file(file_path) # call the function

    # Iterate over each row and count the employees per department
    for row in data:
        department_number = row['department'].strip()  # Access the department field and remove any whitespace using strip()

        # If department not exists in the dictionary, add it with count 1 otherwise,increment its count
        if department_number not in count_department:
            count_department[department_number] = 1 # Department is new, initialize its count to 1
        else:
            count_department[department_number] += 1 # Department exists, increment the count by 1

    return count_department # Return the dictionary containing employee count per department


def get_unique_departments(file_path):
    # Create an empty set to store unique department values
    # A set is used because it automatically removes duplicate values
    unique_departments = set() # Initialize an empty set to hold unique department names

    # Read the CSV data
    data = read_csv_file(file_path) # call the function

    # Iterate over each row
    for row in data:
        # Extract the department value
        department = row('department', '').strip() # remove any whitespace using strip()
        unique_departments.add(department) # Add the department value to the set

    return unique_departments # Return the set containing all unique department names


# This function displays the formatted ouput of the department and the number of employee in each one.
# sorted by employee count in descending order.
def formatted_output_department(counts_department, num_rows):
    # Convert the dictionary to a list of tuples (department, count)
    department_list = list(counts_department.items())

    # Sort by employee count in ascending order (smallest to largest) by iterating over each pair of departments
    for i in range(len(department_list)):  # Outer loop iterates over all elements
        for j in range(i + 1, len(department_list)):  # Inner loop compares each pair of elements (after i)
            if department_list[i][1] > department_list[j][1]:  # Compare the employee count (the second element of each tuple)
                # Swap if the current element has a higher count order from smallest to largest
                department_list[i], department_list[j] = department_list[j], department_list[i]

    # Sort the elements for Largest to Smallest by reversing the order
    department_list.reverse()

    # Print the formatted department report with headers in the same line
    print(f"{'Department':<25}{'  # of Employees':<30}")
    print("--------------             -------------")

    # This loop will print the department names and their employee counts
    for i in range(num_rows):
        department, count = department_list[i]
        print(f"{department:<30}{count:<20}")


# Function to print total employees, sum of salaries, and average salary
def statistics(file_path):
    # Get total number of employees
    data = read_csv_file(file_path)
    total_employees = len(data)

    # Get the sum of salaries
    total_salary = sum_salaries(file_path) # calls the function

    # Get the average salary
    average_salary = average_Salary(file_path) # calls the function

    # Print the formatted statistics
    print("Statistics")
    print("---------------------------------")
    print(f"{'Total number of employees:':<25} {total_employees}")
    print(f"{'Sum of Salaries:':<10} {total_salary:,.2f}")
    print(f"{'Average Salary:':<10} {average_salary:,.2f}")


# Function to count the total number of employees
def count_total_employees(counts_department):
    total_employees = sum(counts_department.values())
    return total_employees


# Function to calculate the total salary
def sum_salaries(file_path):
    total_salary = 0 # Initialize a variable to hold the total salary sum
    # Read the CSV data
    data = read_csv_file(file_path)
    # Iterate over the data and sum the salaries
    for row in data:
        salary = float(row['salary'])  # Access salary
        total_salary += salary  # Add the salary to the total

    return total_salary # Return the total sum of all salaries

# Function to calculate average salary
def average_Salary(file_path):
    total_salary = 0 # Initialize a variable to hold the sum of all salaries
    count = 0 # Initialize a counter to track the number of employees
    # Read the CSV data
    data = read_csv_file(file_path)
    for row in data: # Iterate over each row in the data
        total_salary += float(row['salary']) # Add the salary of the current row to total_salary
        count += 1 # Increment the employee count for each row

    # Calculate the average salary by dividing the total salary by the number of employees
    return total_salary / count # Return the calculated average salary

# --------------------- Task 3 functions ----------------

import json

def load_employees_from_json(filename):
    # Load employees from a JSON file and return a list of company_employees objects.
    employees = [] # Create an empty list to store employee objects
    with open(filename, 'r') as file:
        data = json.load(file)
        for item in data: # Iterate over each item (employee) in the JSON data
            # Create a companyEmployees object using data from the JSON and add it to the employees list
            employees.append(
                companyEmployees(
                    id=item['id'],
                    first_name=item['first_name'],
                    last_name=item['last_name'],
                    email=item['email'],
                    gender=item['gender'],
                    department=item['department'],
                    salary=item['salary'],
                    bonus=item['bonus'],
                    dateOfBirth=item['dateOfBirth']
                )
            )
    return employees # Return the list of employee objects


def display_menu():
    # Display the menu options to the user.
    print("1. Display all the information")
    print("2. Search by <<any attribute>>")
    print("3. Display all rows with a <<numeric attribute>> more than a user-entered value")
    print("4. Exit")

def display_all(employees):
    # Display all employee details
    print("\n--- All Employees ---")
    for emp in employees:
        print(f"ID: {emp.id}, Full Name: {emp.first_name} {emp.last_name}, "
              f"Email: {emp.email}, Gender: {emp.gender}, Department: {emp.department}, "
              f"Salary: ${emp.salary:.2f}, Bonus: ${emp.bonus:.2f}, Date of Birth: {emp.dateOfBirth}")


def search_by_attribute(employees, attribute, value):
    # Search for employees by a specific attribute and value.
    print(f"\n--- Searching by {attribute} = {value} ---")
    # Initialize a flag to track whether any employee matches the search criteria
    found = False # Initially, no match has been found. I set the flag to False.

    # Iterate over each employee in the employees list
    for emp in employees:
        # Check each attribute
        if attribute == "id" and emp.id == int(value):# Check if the search attribute is 'id' and if the employee's id matches the given value
            print(emp) # Print the employee details if match found
            found = True # Set the found flag to True as a match was found
        elif attribute == "first_name" and emp.first_name.lower() == value.lower():
            print(emp)
            found = True
        elif attribute == "last_name" and emp.last_name.lower() == value.lower():
            print(emp)
            found = True
        elif attribute == "email" and emp.email.lower() == value.lower():
            print(emp)
            found = True
        elif attribute == "gender" and emp.gender.lower() == value.lower():
            print(emp)
            found = True
        elif attribute == "department" and emp.department.lower() == value.lower():
            print(emp)
            found = True
        elif attribute == "salary" and emp.salary == float(value):
            print(emp)
            found = True
        elif attribute == "bonus" and emp.bonus == float(value):
            print(emp)
            found = True
        elif attribute == "dateOfBirth" and emp.dateOfBirth == value:
            print(emp)
            found = True
    # If no matching employees are found, print a message
    if not found:
        print("No matching employees found.\n")

def filter_by_numeric_attribute(employees, attribute, given_user_value):
    # Display employees whose numeric attribute is greater than the given user value,
    # using int() or float().
    print(f"\n---- Employees with {attribute} higher than {given_user_value} ----")
    found = False # Initialize a flag to track if any matching employees are found

    for emp in employees: # Iterate over each employee in the employees list
        try:
            # Check if the attribute is 'id' and if the employee's id is greater than the given value
            if attribute == "id" and emp.id > int(given_user_value):
                print(emp) # Print the employee details if they match the condition
                found = True # Set the found flag to True as a match was found
            elif attribute == "salary" and emp.salary > float(given_user_value):
                print(emp)
                found = True
            elif attribute == "bonus" and emp.bonus > float(given_user_value):
                print(emp)
                found = True
        except:
            print("Invalid input.Please enter a valid numeric value for comparison.")
            return
    if not found: # Only display this message after the loop if no employees match
        print("No employees found.")


class companyEmployees: # class attribute
    # Class attribute: Company name
    company_name = "Tech Innovation"

    # initialize an employee object with attributes
    def __init__(self, id: int, first_name: str, last_name: str, email: str,
             gender: str, department: str, salary: float, bonus: float,
             dateOfBirth: str):
       self.id = id
       self.first_name = first_name
       self.last_name = last_name
       self.email = email
       self.gender = gender
       self.department = department
       self.salary = salary
       self.bonus = bonus if bonus else 0.0 # Default to 0.0 if bones is None
       self.dateOfBirth = dateOfBirth

    # Produce a formatted result of all information in the object.
    def __str__(self):
        # String representation of all instance attributes
        output = f"ID: {self.id}, Name: {self.first_name} {self.last_name}, "
        f"Email: {self.email}, Gender: {self.gender}, Department: {self.department}, "
        f"Salary: {self.salary:.2f}, Bonus: {self.bonus:.2f}, DateOfBirth: {self.dateOfBirth}"

        return output

    # Instance method 1
    # Calculate the total annual income for the employee by summing their salary and bonus.
    def calculateAnnualIncome(self):
        annual_income = self.salary + self.bonus
        return annual_income

    # Instance method 2
    # Calculate bonus as a percentage of the salary
    def calculateBonusPercentage(self):
            return (self.bonus / self.salary) * 100
