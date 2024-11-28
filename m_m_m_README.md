# Writing the README content for the Iris dataset analysis script to a file

readme_content = """
# Iris Dataset Analysis

This Python script performs a simple statistical analysis of the Iris dataset and visualizes the results.

## Features

1. **Load Dataset**: Load the Iris dataset from a CSV file.
2. **Data Preview**: Displays the first few rows of the dataset for an overview.
3. **Statistical Analysis**:
   - Calculates the mean, median, and mode of numeric columns in the dataset.
4. **Visualizations**: Generates histograms for each numeric column to show the distribution of values.

## Requirements

- Python 3.x
- Required Python libraries:
  - `pandas`
  - `numpy`
  - `matplotlib`

### Install Required Libraries

Use the following command to install the necessary libraries:

```bash
pip install pandas numpy matplotlib

### Usage
Place your Iris dataset in the specified path and ensure it is named Iris.csv.
Update the script with the correct path to your dataset if needed:
python


df = pd.read_csv('C:\\Path\\To\\Your\\Iris.csv')
Run the script: