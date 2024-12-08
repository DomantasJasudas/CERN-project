import os  # Import os module for directory and file management

def create_LaTeX_table(file_name, data, dir_name='latex_tables'):
    """
    Creates a LaTeX table from the given data (dictonary) and saves it in a specified directory.

    Parameters:
    - file_name (str): Name of the LaTeX file to save the table in.
    - data (dict): Dictionary containing table headers as keys and lists of column values as values.
    - dir_name (str): Name of the directory to save the file in. Defaults to 'latex_tables'.
    """
    
    # Extract headers from the data dictionary and determine the table dimensions
    headers = list(data.keys())  # Get the column headers from the dictionary keys
    num_columns = len(headers)  # Number of columns in the table
    num_rows = max(len(values) for values in data.values())  # Maximum number of rows across all columns

    # Build the LaTeX table as a string
    table_content = [
        "%------------------------------TABLE------------------------------",
        "\\begin{table}[ht!]",  # Begin the table with positioning options
        "\\centering",  # Center the table on the page
        "\\caption{Caption}",  # Placeholder for a caption
        "\\resizebox{0.8\\textwidth}{!}{%",  # Adjust table width to fit within 80% of text width
        "\\begin{tabular}{|" + "|".join(['c'] * num_columns) + "|}",  # Define column alignment (centered) and borders
        "\\hline",  # Top border of the table
        " & ".join(headers) + " \\\\",  # Add headers, separated by "&", and end the row with "\\"
        "\\hline"  # Add a horizontal line under the headers
    ]

    # Populate the table with data row by row
    for i in range(num_rows):
        row_content = []
        for header in headers:
            # If the current row index exceeds the number of values in a column, use a blank space
            value = data[header][i] if i < len(data[header]) else " "
            row_content.append(str(value))  # Convert the value to a string
        
        # Add the row content to the table, separated by "&", and terminate with "\\"
        table_content.append(" & ".join(row_content) + " \\\\")
        table_content.append("\\hline")  # Add a horizontal line after each row

    # Finalize the LaTeX table structure
    table_content.extend([
        "\\end{tabular}",  # End the tabular environment
        "}",  # Close the resizebox environment
        "\\end{table}",  # End the table environment
        "%------------------------------TABLE------------------------------",
        ""
    ])
    
    # Define the folder path for saving the file
    file_location = os.getcwd()  # Get the current working directory
    folder = f'\\{dir_name}'  # Define the folder name (use "\\" for Windows paths)
    folder_path = file_location + folder  # Combine the working directory with the folder name

    # Ensure the directory exists; create it if it doesn't
    try:
        if not os.path.exists(folder_path):  # Check if the folder exists
            os.makedirs(folder_path)  # Create the folder
    except Exception as e:
        print(f"Error creating directory {folder_path}: {e}")  # Handle directory creation errors
        return  # Exit the function if an error occurs

    # Combine the folder path and file name to get the full file path
    file_path = os.path.join(folder_path, file_name)

    # Write the LaTeX table to the file
    try:
        with open(file_path, 'w') as f:
            f.write("\n".join(table_content))  # Write the table content line by line
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")  # Handle file writing errors
