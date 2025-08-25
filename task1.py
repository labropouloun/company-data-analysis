# step1
# Nancy Lampropoulou
# This program reads employee data from a CSV file, processes it by combining first and last names,
# sorts the data by full name, validates user input for the number of rows to display,
# and formats the specific data for output.

from companydata_analysis import read_csv_to_list, sort_by_name, validate_row_input, format_data

def main():
     # Default filename
     default_filename = "CompanyData.csv"

     # Infinite loop to keep asking the user for input until valid data is processed
     while True:
          # Prompt the user for a filename or allow them to use the default
          filename = input(f"Enter the filename (or press Enter to use the default: {default_filename}): ")

          # If the user presses Enter without typing anything, use the default filename
          if not filename:
               filename = default_filename

          # Open the specified file in read mode ('r') using the 'with' statement.
          with open(filename, 'r') as file:
            # Load data from CSV into a list of lists
            data = read_csv_to_list(filename) # call the function

            # Sort the data by full name
            sorted_data = sort_by_name(data) # call the function

            # Validate user input for the number of rows to display
            num_rows = validate_row_input() # call the function

            # Display the formatted output
            format_data(sorted_data, num_rows) # call the function
            break  # Exit the loop after processing the file

if __name__ == "__main__":
    main()
