class Movie:
    def __init__(self, title, director, release_year):
        self.title = title
        self.director = director
        self.release_year = release_year

    def display_info(self):
        return  f"{self.title} director: {self.director}, release year: {self.release_year}"

    def is_classic(self):
        return 2024 - self.release_year > 30

my_movie = Movie('My Movie', 'My Movie', 1999)
my_movie2 = Movie('Pulp Fiction', 'Quentin Tarantion', 1994)

print(my_movie.title)
print(my_movie2.title)
print(my_movie.director)
print(my_movie2.director)

print()

print(my_movie.display_info())
print(my_movie2.display_info())



