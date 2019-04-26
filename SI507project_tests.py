from flask import Flask
from SI507_final_project import Movie_Recommend, create_type

def main():
    n = Movie_Recommend.movie_randomselect()
    print(n)
    m = create_type(Drama)
    print(m)

if __name__ == "__main__":
    main()