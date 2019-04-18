from flask import Flask
from SI507project_tools import Movie_Recommend

m = Movie_Recommend.movie_total_number()
print(m)

n = Movie_Recommend.movie_randomselect(6)
print(n)
