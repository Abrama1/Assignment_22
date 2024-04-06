import json

# Load the JSON data from the file
with open("movies.json", "r") as file:
    data = json.load(file)

# Filter movies released after 2000 and genre is Crime
new_crime_movies = [movie for movie in data[0]["results"] if movie.get("release_date", "").split('-')[0] > '2000' and 'Crime' in movie.get("genres", [])]
for movie in new_crime_movies:
    movie["genres"] = [genre.replace("Crime", "New_Crime") for genre in movie.get("genres", [])]

# Filter movies released before 2000 and genre is Drama
old_drama_movies = [movie for movie in data[0]["results"] if movie.get("release_date", "").split('-')[0] < '2000' and 'Drama' in movie.get("genres", [])]
for movie in old_drama_movies:
    movie["genres"] = [genre.replace("Drama", "Old_Drama") for genre in movie.get("genres", [])]


# Filter movies released in 2000 and add New_Century to genres
for page_data in data:
    for movie in page_data["results"]:
        if movie.get("release_date", "").startswith('2000'):
            if 'New_Century' not in movie.get("genres", []):
                movie["genres"].append("New_Century")

# Rewrite the modified JSON data back to the file
with open("movies.json", "w") as file:
    json.dump(data, file, indent=4)
