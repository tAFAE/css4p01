# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 15:02:32 2024

@author: ptmab
"""

import pandas as pd
#to read the file.TPM
file = pd.read_csv("movie_dataset.csv")
df = pd.read_csv("movie_dataset.csv", index_col=0)
print(df.info())
#to replace all the nans in the code.TPM
df.dropna(inplace = True)
df = df.reset_index(drop=True)
#to remove the spaces.TPM
df.columns = df.columns.str.replace( "", "_")
# Handle missing values fill missing values with mean for numeric columns and mode for categorical columns.TPM
#df.fillna(df.mean(), inplace=True)  # Replace NaN values with mean for numeric columns.TPM
#df.fillna(df.mode().iloc[0], inplace=True)  # Replace NaN values with mode for categorical columns.TPM
print(df.info())
print(df.describe())
# define highest rates movie.TPM
highest_rated_movie_index = df["_R_a_t_i_n_g_"].idxmax()

# Get the details of the highest rated movie.TPM
highest_rated_movie = df.loc[highest_rated_movie_index]

# Print the result.TPM
print("The highest rated movie in the dataset is:")
print(highest_rated_movie[["_T_i_t_l_e_", "_R_a_t_i_n_g_"]])

#  define the average revenue.TPM
average_revenue = df["_R_e_v_e_n_u_e_ _(_M_i_l_l_i_o_n_s_)_"].mean()

# Print the result.TPM
print(f"The average revenue of all movies in the dataset is: ${average_revenue:.2f}")

#define the start and end year.TPM
start_year = 2015
end_year = 2017

# Filter movies released between 2015 and 2017.TPM
filtered_movies = df[(df["_Y_e_a_r_"] >= start_year) & (df["_Y_e_a_r_"] <= end_year)]

# Calculate the average revenue for the filtered subset.TPM
average_revenue_2015_to_2017 = filtered_movies["_R_e_v_e_n_u_e_ _(_M_i_l_l_i_o_n_s_)_"].mean()

# Print the result.TPM
print(f"The average revenue of movies from {start_year} to {end_year} in the dataset is: ${average_revenue_2015_to_2017:.2f}")

#define the year count for 2016.TPM
year_2016_count = df["_Y_e_a_r_"].value_counts().get(2016, 0)

# Print the result.TPM
print(f"The number of movies released in the year 2016 is: {year_2016_count}")

#define director name.TPM
director_name = 'Christopher Nolan'

# Filter movies directed by Christopher Nolan.TPM
nolan_movies_count = df[df["_D_i_r_e_c_t_o_r_"] == director_name].shape[0]

# Print the result.TPM
print(f"The number of movies directed by {director_name} is: {nolan_movies_count}")

#define minimum rating.TPM
minimum_rating = 8.0

# Filter movies with a rating of at least 8.0.TPM
high_rated_movies_count = df[df["_R_a_t_i_n_g_"] >= minimum_rating].shape[0]

# Print the result.TPM
print(f"The number of movies with a rating of at least {minimum_rating} is: {high_rated_movies_count}")


# Filter movies directed by Christopher Nolan.TPM
nolan_movies = df[df["_D_i_r_e_c_t_o_r_"] == director_name]

# Calculate the median rating for the filtered subset.TPM
median_rating_nolan_movies = nolan_movies['_R_a_t_i_n_g_'].median()

# Print the result.TPM
print(f"The median rating of movies directed by {director_name} is: {median_rating_nolan_movies:.2f}")

# DEFINE average rating by year.TPM
average_rating_by_year = df.groupby("_Y_e_a_r_")['_R_a_t_i_n_g_'].mean()

# Find the year with the highest average rating.TPM
year_highest_average_rating = average_rating_by_year.idxmax()

# Print the result.TPM
print(f"The year with the highest average rating is: {year_highest_average_rating}")

# define the range.TPM
start_year1 = 2006
end_year2 = 2016

# Filter movies released between 2006 and 2016.TPM
movies_2006_to_2016 = df[(df["_Y_e_a_r_"] >= start_year1) & (df["_Y_e_a_r_"] <= end_year2)]

# Calculate the number of movies for each year.TPM
movie_count_by_year = movies_2006_to_2016.groupby("_Y_e_a_r_").size()

# Find the counts for 2006 and 2016.TPM
count_2006 = movie_count_by_year.get(2006, 0)
count_2016 = movie_count_by_year.get(2016, 0)

# Calculate the percentage increase.TPM
percentage_increase = ((count_2016 - count_2006) / count_2006) * 100

# Print the result.TPM
print(f"The percentage increase in the number of movies between {start_year1} and {end_year2} is: {percentage_increase:.2f}%")

#these instructions did not work.TPM 
# define most common actor. TPM
#most_common_actor = df["_A_c_t_o_r_s_"].mode().iloc[0]
#most_common_actors = df['_A_c_t_o_r_s_'].mode().tolist()
#most_common_actors = df['_A_c_t_o_r_s_'].value_counts().idxmax()

# Print the result.TPM
#print(f"The most common actor in all the movies is: {most_common_actor}")
#print(f"The most common actor in all the movies is/are: {most_common_actors}")

#to try again we use.TPM 

actors_series = df['_A_c_t_o_r_s_']

# Split and flatten the actors' names.TPM
all_actors = [actor.strip() for actors_list in actors_series.str.split(',') for actor in actors_list]

# Create a pandas Series from the flattened list.TPM
all_actors_series = pd.Series(all_actors)

# Get the most common actor(s).TPM
most_common_actor = all_actors_series.value_counts().idxmax()

# Print the result.TPM
print(f"The most common actor in all the movies is: {most_common_actor}")

# DEFINE GENRE SERIES.TPM
genres_series = df["_G_e_n_r_e_"]
# Split and flatten the genres
all_genres = [genre.strip() for genres_list in genres_series.str.split(',') for genre in genres_list]

# Get the count of unique genres.TPM
unique_genres_count = len(set(all_genres))

# Print the result.TPM
print(f"The number of unique genres in the dataset is: {unique_genres_count}")

# Assuming 'df' is your DataFrame and you want to analyze numerical columns.TPM
numerical_features = df.select_dtypes(include=['float64', 'int64'])

# Calculate the correlation matrix.TPM
correlation_matrix = numerical_features.corr()

# Print the correlation matrix.TPM
print("Correlation Matrix:")
print(correlation_matrix)

# Insights:
# 1. Look for strong positive or negative correlations between pairs of features.
# 2. Identify features with high positive correlation, as changes in one may positively influence the other.
# 3. Identify features with high negative correlation, as changes in one may negatively influence the other.
# 4. Features with correlation close to zero are weakly correlated.
# 5. Consider the practical implications of strong correlations for decision-making.

# Additional Advice:
# Directors can consider the following advice based on insights:
# - If two features are highly positively correlated, emphasizing one might enhance the other.
# - If two features are highly negatively correlated, balancing them may be crucial.
# - Understanding correlations can help in strategic decision-making during film production.

# Note: Interpretation of correlations requires domain-specific knowledge.

