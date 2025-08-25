# Task2
# Nancy Lampropoulou
# This program processes a CSV file containing employee data, read the information in a list of dictionaries,
# provides department statistics, validates user input for the number of rows to display,
# and calculates total, average salaries and the number of employees in each department.


from companydata_analysis import read_csv_file, count_employees_per_department, formatted_output_department, validate_row_input, statistics

def main():
    # Path to CSV file
    file_path = 'CompanyData.csv'

    # Call the function to read the CSV file and get the data
    data = read_csv_file(file_path)

    # Print out the list of dictionaries for validation
    for row in data:
        print(row)
    # Get the count of employees per department
    counts_department = count_employees_per_department(file_path) # calls the function

    # Validate user input for the number of rows to display
    num_rows = validate_row_input() # call the function

    # Call the function to print the department and the number of employee in each one with specific rows
    formatted_output_department(counts_department, num_rows)

    # Call the statistics function to display the formatted output
    statistics(file_path)

if __name__ == "__main__":
    main()
