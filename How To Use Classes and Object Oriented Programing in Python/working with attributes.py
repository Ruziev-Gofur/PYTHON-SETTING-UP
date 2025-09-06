class Movie:
    def __init__(self, title, director, release_year):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.view_count = 0

    def display_info(self):
        return  f"{self.title} director: {self.director}, release year: {self.release_year}"

    def is_classic(self):
        return 2024 - self.release_year > 30

    def check_views(self):
        return f"{self.title} was viewed: {self.view_count}"

    def update_view(self, views):
        if views > self.view_count:
            self.view_count = views
        else:
            print('Views don\'t dissapear')

    def increment_views(self, view_to_add):
        self.view_count += view_to_add

movie1 = Movie("The Shawshank Redemption", "Frank Darabont", 1994)
print(movie1.display_info())
print(movie1.check_views())

print("\nAfter a few people watched the movie")
movie1.view_count = 20
print(movie1.check_views())

print("\nAfter even MORE people watched the movie")
movie1.update_view(30)
print(movie1.check_views())

print("\nAfter even MORE people watched the movie")
movie1.update_view(10)
print(movie1.check_views())

print("\nAfter even MORE people watched the movie")
movie1.increment_views(200)
movie1.view_count += 300
print(movie1.check_views())



