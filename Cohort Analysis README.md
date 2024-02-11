# Online Retail Cohort Analysis

## Overview

Python script for conducting cohort analysis on an Online Retail dataset. Analyzes customer retention rates and average quantity metrics over time to gain insights into customer behavior.

## Getting Started

1. **Clone Repository:**
   - Clone this repository to your local machine:

     ```bash
     git clone https://github.com/your-username/online-retail-cohort-analysis.git
     ```

2. **Install Dependencies:**
   - Ensure you have the required libraries installed:

     ```bash
     pip install numpy pandas matplotlib seaborn scikit-learn
     ```

3. **Run the Script:**
   - Execute the Python script:

     ```bash
     python cohort_analysis.py
     ```

## Dataset

The script uses the 'Online Retail.xlsx' dataset for analysis. Make sure the dataset is in the project directory.

## Results and Insights

- **Retention Rates Heatmap:** Visualizes customer retention rates over time.
- **Average Quantity Heatmap:** Illustrates the average quantity metrics for each cohort.

## Data Cleaning

- Handles missing values by removing rows with missing CustomerID.
- Checks and removes duplicate data.
- Filters out rows with negative Quantity or UnitPrice.

## Cohort Analysis

- Prepares data for cohort analysis by assigning cohorts based on customer registration months.
- Calculates and visualizes retention rates and average quantity for each cohort.

## Visualization

- Utilizes Matplotlib and Seaborn to create visually appealing heatmaps.

Feel free to explore and adapt the script to analyze your own retail datasets.

