```markdown
# Online Retail Cohort Analysis

## Overview

This Python script conducts cohort analysis on an Online Retail dataset. It visualizes customer retention rates and average quantity metrics over time, providing insights into customer behavior.

## Prerequisites

Make sure you have the required libraries installed:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/online-retail-cohort-analysis.git
   ```

2. Navigate to the project directory:

   ```bash
   cd online-retail-cohort-analysis
   ```

3. Run the script:

   ```bash
   python cohort_analysis.py
   ```

## Dataset

The script uses the 'Online Retail.xlsx' dataset for analysis. Ensure the dataset is in the project directory.

## Results

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

- Uses Matplotlib and Seaborn for creating visually appealing heatmaps.

Feel free to explore and adapt the script to analyze your own retail datasets.

```

This README provides a brief overview of the script, outlines prerequisites, and guides users on how to get started and interpret the results.
