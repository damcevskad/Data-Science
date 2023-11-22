import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("netflix_data.csv")

netflix_subset = netflix_df[netflix_df['type'] == 'Movie']
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

short_movies = netflix_movies[netflix_movies['duration'] < 60]

colors = []
for col, row in netflix_movies.iterrows():
    if row['genre'] == 'Children':
        colors.append('yellow')
    elif row['genre'] == 'Documentaries':
        colors.append('purple')
    elif row['genre'] == 'Stand-Up':
        colors.append('orange')
    else:
        colors.append('blue')

fig = plt.figure(figsize=(12, 8))
plt.title('Movie Duration by Year of Release')
plt.xlabel('Release Year')
plt.ylabel('Duration (min)')

plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)
plt.show()
