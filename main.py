# MOVIE RECOMMENDATION SYSTEM [BASED ON GENRE AND RATING]

import random
from movieList import movies

def get_genre():
    while True:
        print("ENTER THE GENRE OF YOUR CHOICE [form 'ACTION' , 'DRAMA' , 'COMEDY' , 'FANTASY' and 'SCI-FI' ] : ")
        genre = input().strip()
        if genre.isalpha():
            return genre.capitalize()
        else:
            print("Invalid input. Please enter a valid genre [form 'ACTION' , 'DRAMA' , 'COMEDY' , 'FANTASY' and 'SCI-FI' ] !")


def get_rating():
    print("ENTER THE RATING OF YOUR CHOICE (from 5 to 10) : ")
    while True:
        rating = input()
        try:
            rating = float(rating)
            if 5.0 <= rating <= 10.0:
                return rating
            else:
                print("Invalid rating. Please enter a number between 5 and 10.")

        except:
            print("Invalid rating. Please enter a valid number between 5.0 and 10.0")

preferred_genre = get_genre()
preferred_rating = get_rating()

print("\nUSER PREFERRED GENRE : {}".format(preferred_genre))
print("USER PREFERRED RATING : {}\n".format(preferred_rating))

# filtering the movies based on user preferrance

def filter_movie_from_list(movie_list , genre , rating):
    filtered_movies = []
    for movie in movie_list:
        if movie["genre"] == preferred_genre and round(movie["rating"]) == round(preferred_rating) :
            filtered_movies.append(movie)
    return filtered_movies

def recommend_movies(filtered_movies):
    if filtered_movies:
        return random.choice(filtered_movies)
    else:
        return None
    

def main():
    print("WELCOME TO THE MOVIE RECOMMENDATION SYSTEM !\n")

    recommended_movies_by_filtering = filter_movie_from_list(movies,preferred_genre,preferred_rating)

    recommended_movie = recommend_movies(recommended_movies_by_filtering)

    if recommended_movie:
        print("WE RECOMMEND THE FOLLOWING MOVIE :")
        
        print(recommended_movie['title'] + "(GENRE : " + recommended_movie['genre'] + "  AND   RATING : "+str(recommended_movie['rating']) + " )\n")

    else:
        print("SORRY , NO MOVIES MATCH YOUR CRITERIA.\n")

main()