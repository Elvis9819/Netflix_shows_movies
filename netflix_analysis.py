import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('netflix_data.csv')

# Data Cleaning: Address missing values
df.fillna('Unknown', inplace=True)

# Data Exploration: Describe the data
data_description = df.describe(include='all')
print(data_description)

# Data Visualization: Most watched genres
plt.figure(figsize=(12, 6))
sns.countplot(y='listed_in', data=df, order=df['listed_in'].value_counts().index)
plt.title('Most Watched Genres')
plt.xlabel('Count')
plt.ylabel('Genres')
plt.show()

# Data Visualization: Ratings distribution
plt.figure(figsize=(12, 6))
sns.countplot(x='rating', data=df, order=df['rating'].value_counts().index)
plt.title('Ratings Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

# Save the plots
plt.savefig('ratings_distribution.png')
plt.savefig('most_watched_genres.png')