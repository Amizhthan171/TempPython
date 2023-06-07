import pandas as pd
import os
from multiprocessing import Pool

# Function to check file existence
def check_file_exists(file_path):
    return os.path.exists(file_path)

# Main function
if __name__ == '__main__':
    # Directory containing the CSV files
    directory = 'path/to/your/csv/directory'

    # Get the list of CSV files in the directory
    csv_files = [file for file in os.listdir(directory) if file.endswith('.csv')]

    # Number of processes to utilize
    num_processes = 4

    for csv_file in csv_files:
        # Construct the full path to each CSV file
        file_path = os.path.join(directory, csv_file)

        # Read the CSV file
        df = pd.read_csv(file_path)

        # Split the DataFrame into chunks
        chunks = np.array_split(df, num_processes)

        # Create a process pool
        with Pool(processes=num_processes) as pool:
            # Process each chunk in parallel
            results = pool.map(check_file_exists, [chunk['FilePath'] for chunk in chunks])

        # Concatenate the results and add as a new column in the DataFrame
        df['Exists'] = pd.concat(results)

        # Continue processing the dataframe with the existence status