# %%
# Task 1
movies = [{'title': 'The Shawshank Redemption', 'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 'genre': 'Drama', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY67_CR0,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'}, {'title': 'The Godfather', 'description': 'The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son.', 'genre': 'Crime', 'image_url': 'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY67_CR1,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0068646/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_2'}, {'title': 'The Dark Knight', 'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.', 'genre': 'Action', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY67_CR0,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0468569/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_3'}, {'title': 'The Godfather: Part II', 'description': 'The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.', 'genre': 'Crime', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMWMwMGQzZTItY2JlNC00OWZiLWIyMDctNDk2ZDQ2YjRjMWQ0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY67_CR1,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0071562/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_4'}, {'title': '12 Angry Men', 'description': 'The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.', 'genre': 'Crime', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_UX45_CR0,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0050083/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_5'}]

list_of_movies = len(movies)
print(list_of_movies)

# Task 2
movie_1 = movies[0]
print(movie_1)
print(type(movie_1))

# Task 3
new_dict = {}
for d in movies:
  for key, value in d.items():
    if key in new_dict:
      new_dict[key].append(value)
    else: 
      new_dict[key] = [value]

for key in new_dict:
  print(new_dict[key][0])

# %%
movies = [{'title': 'The Shawshank Redemption', 'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 'genre': 'Drama', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY67_CR0,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'}, {'title': 'The Godfather', 'description': 'The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son.', 'genre': 'Crime', 'image_url': 'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY67_CR1,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0068646/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_2'}, {'title': 'The Dark Knight', 'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.', 'genre': 'Action', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY67_CR0,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0468569/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_3'}, {'title': 'The Godfather: Part II', 'description': 'The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.', 'genre': 'Crime', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMWMwMGQzZTItY2JlNC00OWZiLWIyMDctNDk2ZDQ2YjRjMWQ0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY67_CR1,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0071562/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_4'}, {'title': '12 Angry Men', 'description': 'The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.', 'genre': 'Crime', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_UX45_CR0,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0050083/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_5'}]
# Task 1
def print_every_movie_title(movies):
    for movie in movies:
        print(movie['title'])

# Task 2
def get_movie_description_length(movie):
  return len(movie['description'])

# Task 3
num_of_movies = len(movies)

def get_movie_description_length(movie):
  return len(movie['description'])

def get_avg_movie_description_length():
    sum = 0
    for movie in movies:
        sum += get_movie_description_length(movie)
    return round(float(sum) / num_of_movies, 1)

get_avg_movie_description_length()


# %%
# Task 1
import json

def load_movies_data():
  with open('movies.json', 'r') as f:
    movies = json.load(f)
  return movies 

movies = load_movies_data() #This will first load the movies from the 'movies.json' file using the load_movies_data function.
print(movies)

# Task 2

def get_unique_genres():
    genres = set()
    for movie in movies:
        genres.add(movie['genre'])
    return genres

unique_genres = get_unique_genres()
print(unique_genres)

# Task 3

def get_movies_in_genre(movies, genre):
   movie_genre = []
   for movie in movies:
      if movie.get('genre') == genre: #The get() method returns the value of the item with the specified key.
         movie_genre.append(movie)
   return movie_genre

get_movies_in_genre(movies, 'Drama')

# %%
movies = [{'title': 'The Shawshank Redemption', 'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 'genre': 'Drama', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY67_CR0,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'}, {'title': 'The Godfather', 'description': 'The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son.', 'genre': 'Crime', 'image_url': 'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY67_CR1,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0068646/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_2'}, {'title': 'The Dark Knight', 'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.', 'genre': 'Action', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY67_CR0,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0468569/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_3'}, {'title': 'The Godfather: Part II', 'description': 'The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.', 'genre': 'Crime', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMWMwMGQzZTItY2JlNC00OWZiLWIyMDctNDk2ZDQ2YjRjMWQ0XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY67_CR1,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0071562/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_4'}, {'title': '12 Angry Men', 'description': 'The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.', 'genre': 'Crime', 'image_url': 'https://m.media-amazon.com/images/M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_UX45_CR0,0,45,67_AL_.jpg', 'link': 'https://imdb.com/title/tt0050083/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=VZEYAR8ZVPNKZ9V7MV87&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_5'}]

def get_unique_genres(movies):
    genres = set()
    for movie in movies:
        genres.add(movie['genre'])
    return genres

get_unique_genres(movies)
print(get_unique_genres(movies))

# %%
def get_unique_genres(movies):
    genres = set()
    for movie in movies:
        genres.add(movie['genre'])
    return genres

unique_genres = get_unique_genres(movies)
print(set(unique_genres))

# %%
name = ('what is your name? ')

assert name == 'John', 'You are not John'
print('Hello, John')


# %%
name = input("")
age = input("")

assert name == "John" or age == "20", "You are not John"
print('Hello, John')

## assert isinstance(age, int), "Age is not a number"
## print("Age is a number")

try:
   int(age)
   print('Age is a number')
except ValueError:
   print('Age is not a number')


# %%
x = 'Dog'
y = 'Cat'
z = x + ' ' + y

lenz = len(z) # Obtain the number of characters of z
print(lenz)

print(len(y)) # Obtain the number of characters of y

my_ls = z.split() # Separate each word of z and store the result in a list
print(my_ls[2]) # Print the second element in the list
# %%

x = "Dog"
y = "cat"
length = len(x)
print(length)

# %%
