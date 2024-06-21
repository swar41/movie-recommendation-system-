
# Movie Recommendation System

This is a Movie Recommendation System built using Flask. The system utilizes two CSV files (`movies.csv` and `ratings.csv`) to provide movie recommendations based on user preferences.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Result](#Result)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Features

- User can select their favorite movies.
- Provides movie recommendations based on selected movies using KNN algorithm (i.e. Cosine-similarity)
- Utilizes collaborative filtering for recommendations.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/swar41/movie-recommendation-system.git
    cd movie-recommendation-system
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install numpy pandas scikit flask
    ```

4. Place the `movies.csv` and `ratings.csv` files in the root directory of the project.

## Usage

1. Run the Flask application:

    ```bash
    python app run.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000`.

3. Select your favorite movies from the list and get recommendations.

## Dataset

The application uses two datasets:

- `movies.csv`: Contains movie information such as movieId, title, and genres.
- `ratings.csv`: Contains user ratings for different movies, including userId, movieId, rating, and timestamp.

Ensure both files are placed in the root directory of the project before running the application.

## Result
![image](https://github.com/swar41/movie-recommendation-system-/assets/141357728/17a4e7d3-9ed2-4ee6-9957-f91134d0e481)
![image](https://github.com/swar41/movie-recommendation-system-/assets/141357728/c5a4d1d2-f9a1-42e9-8e1a-fa29d82d20eb)


## Technologies Used

- Python
- Flask
- Pandas
- Scikit-learn

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add some YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

