# Task3
# Nancy Lampropoulou
# This program manages employee data for a company, loads data from a JSON file allowing the user to display all employee details,
# to search for employees by specific attributes, to filter employees based on numeric criteria and exit the program.

from companydata_analysis import load_employees_from_json, display_menu, display_all, search_by_attribute, filter_by_numeric_attribute, companyEmployees

def main():
    # Load employees from the JSON file
    filename = "company_data.json"
    employees = load_employees_from_json(filename)

    while True: # an infinite loop to keep showing the menu to the user until types 4.
        display_menu() # call the function
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_all(employees) # call the function
        elif choice == '2':
            attribute = input("Enter the attribute to search by (id, first_name, last_name, department, email, gender, salary, bonus, dateOfBirth): ").strip()
            value = input(f"Enter the value for {attribute}: ").strip()
            search_by_attribute(employees, attribute, value) # call the function
        elif choice == '3':
            attribute = input("Enter the attribute you want to search for a numeric value(id, salary, bonus): ").strip()
            try:
                given_user_value = float(input(f"Enter the minimum value for {attribute}: "))
                filter_by_numeric_attribute(employees, attribute, given_user_value) # call the function
            except:
                print("Invalid entered value. Please enter a numeric value.")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
