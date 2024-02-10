#1
def smovie(movie):
  return movie['imdb'] > 5.5

#2 
def submovie(movies):
  return [movie for movie in movies if smovie(movie)]

#3
def category(movies, category):
    return [movie for movie in movies if movie["category"] == category]
  
#4
def aveimdb(movies):
    if not movies:
        return 0
    total = sum(movie["imdb"] for movie in movies)
    return total / len(movies)
  
#5
def averimdbcategory(movies, categoryn):
    categormov = (category(movies, categoryn))
    return aveimdb(categormov)
  
# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

print(smovie({"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"}))

print(submovie(movies))

print(category(movies, "Romance"))

print(aveimdb(movies))

print(averimdbcategory(movies, "Romance"))


