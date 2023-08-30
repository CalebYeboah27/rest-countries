import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load variables from .env file into environment
load_dotenv()
api_bearer_token = os.getenv('API_BEARER_TOKEN')
# print(api_bearer_token)

# receive user inputs
movie_genre = input("your preferred movie genre: ")
watch_region = input("which region of the world are you watching from: ")
origin_country = input("country of origin: ")
# watch_region = "Africa"
# origin_country = "US"


url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=true&language=en-US&page=1&sort_by=popularity.desc&watch_region={watch_region}&with_genres={movie_genre}&with_origin_country={origin_country}"

headers = {
    "accept": "application/json",
    "Authorization": api_bearer_token
}


def recommend_movies():
    # fetch movie data from the api
    movies = requests.get(url, headers=headers)
    response = movies.json()
    # check for movie response
    if (response['total_results'] < 1):
        print("No movies found")
    else:
        titles = []
        overview = []
        release_dates = []
        vote_count = []
        vote_average = []
        adult = []
        # iterate to extract movie data
        for movie in response['results']:
            print(
                f"{movie['original_title']}, released on: {movie['release_date']}"),
            titles.append(movie['original_title'])
            overview.append(movie['overview'])
            release_dates.append(movie['release_date'])
            vote_count.append(movie['vote_count'])
            vote_average.append(movie['vote_average'])
            adult.append(movie['adult'])

    # Converting list to dataframe
    excel_data = {'titles': titles, 'overview': overview,
                  'release dates': release_dates, 'vote count': vote_count,
                  'vote average': vote_average, 'adult': adult}
    df = pd.DataFrame(excel_data)

    # writting to excel
    excel_file_path = 'F:\AzubiAfrica\Projects\Python\\rest_countries\movies.xlsx'
    df.to_excel(excel_file_path, index=False)


recommend_movies()
