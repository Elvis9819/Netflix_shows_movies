# Load necessary libraries
library(ggplot2)

# Load the dataset
df <- read.csv('netflix_data.csv')

# Data Cleaning: Address missing values
df[is.na(df)] <- 'Unknown'

# Data Visualization: Ratings distribution
ggplot(df, aes(x=rating)) +
  geom_bar() +
  ggtitle('Ratings Distribution') +
  xlab('Rating') +
  ylab('Count') +
  theme_minimal()

# Save the plot
ggsave('ratings_distribution_r.png')

