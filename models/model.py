import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
def load_data():
    # Adjust the path if necessary
    movies = pd.read_csv('movies.csv')
    ratings = pd.read_csv('ratings.csv')
    return movies, ratings

# Create a utility matrix
def create_utility_matrix(ratings):
    utility_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating')
    return utility_matrix.fillna(0)

# Get movie recommendations based on user preferences
def get_recommendations(preferences):
    movies, ratings = load_data()
    utility_matrix = create_utility_matrix(ratings)
    movie_similarity = cosine_similarity(utility_matrix.T)
    similarity_df = pd.DataFrame(movie_similarity, index=utility_matrix.columns, columns=utility_matrix.columns)

    similar_scores = pd.Series(dtype='float64')
    for movie in preferences:
        if movie in movies['title'].values:
            movie_id = movies[movies['title'] == movie]['movieId'].values[0]
            similar_scores = pd.concat([similar_scores, similarity_df[movie_id]])
    
    similar_scores = similar_scores.groupby(similar_scores.index).mean()
    similar_scores = similar_scores.sort_values(ascending=False).head(10)

    recommended_movie_ids = similar_scores.index.values
    recommended_movies = movies[movies['movieId'].isin(recommended_movie_ids)]['title'].values
    return recommended_movies
