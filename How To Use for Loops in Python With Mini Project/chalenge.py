movies = [
    'The Shawshank Rede',
    'The Goodfather',
    'The Henry',
    '12 Angry Men',
    "Schindler's List",
    'Pulp Fiction',
    'Fight Club',
    'Forrest Gump'
]
# 1. Print out the movies in a sentence
for movie in movies:
    print(f"My favorite movies is {movie}")

# 2. First 4, last 3, and 2 to 5 movies
print("First 4: ", movies[:4])
print("Last 3: ", movies[7:])
print("Movies 2 to 5: ", movies[2:5])

# 3. Create a list of numbers
numbers = []
for i in  range(1, len(movies) + 1):
    numbers.append(i)
print(numbers)

# 4. Print out the movies names from the list of tuples
# for movies_tuple in numbers_movie_tuples:
#     print(f"I love watching {movies_tuple[1]}")








