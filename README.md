# Netflix Data Analysis

## Assignment Description

This assignment involves analyzing a dataset of Netflix shows and movies to gain insights through data preparation, cleaning, exploration, and visualization.

## Files

- `netflix_analysis.py`: Python script for data preparation, cleaning, exploration, and visualization.
- `netflix_visualization.R`: R script for integrating one of the visualizations.
- `netflix_data.csv`: The dataset used for analysis.

## Instructions

### Python Script

1. Ensure you have the necessary Python libraries installed:
   ```sh
   pip install pandas seaborn matplotlib
   ```

2. Run the Python script:
   ```sh
   python netflix_analysis.py
   ```

3. The script will generate visualizations for the most watched genres and ratings distribution.

### R Script

1. Ensure you have the necessary R libraries installed:
   ```r
   install.packages("ggplot2")
   ```

2. Run the R script:
   ```r
   source('netflix_visualization.R')
   ```

3. The script will generate a visualization for the ratings distribution.

## Data Preparation

- The dataset is loaded from `netflix_data.csv`.
- Missing values are addressed by filling them with 'Unknown'.

## Data Exploration

- The dataset is described, and statistical analysis is performed.

## Data Visualization

- Visualizations for the most watched genres and ratings distribution are created using Python libraries (Seaborn, Pyplot, and Matplotlib).
- One of the visualizations (ratings distribution) is integrated into R.

## Submission

Submit your work as a zipped file or a link to your GitHub repository, along with this README file containing instructions for accessing and understanding your code.