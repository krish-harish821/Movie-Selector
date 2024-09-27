import datetime


def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age


def recommend_movies(age, movie_type):
    recommendations = {
        "action": {
            "child": ["The Incredibles", "Spider-Man: Into the Spider-Verse", "Big Hero 6", "The Lego Movie",
                      "Kung Fu Panda", "Megamind"],
            "teen": ["The Avengers", "Guardians of the Galaxy", "Mad Max: Fury Road", "Spider-Man: Homecoming",
                     "Black Panther", "Thor: Ragnarok"],
            "adult": ["Die Hard", "The Dark Knight", "Inception", "John Wick", "Gladiator",
                      "Terminator 2: Judgment Day"]
        },
        "comedy": {
            "child": ["Toy Story", "Despicable Me", "Shrek", "The Lego Movie 2", "Finding Dory", "Monsters, Inc."],
            "teen": ["Superbad", "Pitch Perfect", "The Hangover", "Mean Girls", "Napoleon Dynamite", "21 Jump Street"],
            "adult": ["Groundhog Day", "Anchorman", "Monty Python and the Holy Grail", "Step Brothers", "Bridesmaids",
                      "Dumb and Dumber"]
        },
        "romance": {
            "child": ["Beauty and the Beast", "Cinderella", "Enchanted", "Frozen", "Tangled",
                      "The Princess and the Frog"],
            "teen": ["The Fault in Our Stars", "10 Things I Hate About You", "Twilight",
                     "To All the Boys I've Loved Before", "A Walk to Remember", "The Perks of Being a Wallflower"],
            "adult": ["Pride and Prejudice", "The Notebook", "La La Land", "Titanic", "Before Sunrise",
                      "Crazy Rich Asians"]
        },
        "horror": {
            "teen": ["A Quiet Place", "The Conjuring", "It", "Insidious", "The Ring", "The Grudge"],
            "adult": ["Hereditary", "Get Out", "The Exorcist", "The Shining", "Psycho", "Silence of the Lambs"]
        },
        "adventure": {
            "child": ["Moana", "Up", "Finding Nemo", "Zootopia", "The Jungle Book", "Peter Pan"],
            "teen": ["Jurassic Park", "The Hunger Games", "Pirates of the Caribbean", "The Maze Runner", "Divergent",
                     "Percy Jackson & the Olympians"],
            "adult": ["Indiana Jones: Raiders of the Lost Ark", "The Lord of the Rings: The Fellowship of the Ring",
                      "The Revenant", "Mad Max: Fury Road", "Avatar", "Interstellar"]
        }
    }

    if age < 13:
        age_group = "child"
        available_movie_types = ["action", "comedy", "romance", "adventure"]
    elif 13 <= age < 18:
        age_group = "teen"
        available_movie_types = ["action", "comedy", "romance", "horror", "adventure"]
    else:
        age_group = "adult"
        available_movie_types = ["action", "comedy", "romance", "horror", "adventure"]

    return recommendations.get(movie_type, {}).get(age_group, []), age_group, available_movie_types


def get_user_birth_year():
    while True:
        birth_year_input = input("Enter your birth year: ")
        if birth_year_input.isdigit() and 1900 <= int(birth_year_input) <= datetime.datetime.now().year:
            return int(birth_year_input)
        else:
            print("Please enter a valid birth year.")


def get_user_movie_type(available_movie_types):
    print(f"What type of movie would you like to watch? Your options are: {', '.join(available_movie_types)}.")
    while True:
        movie_type = input("Please enter your choice: ").lower()
        if movie_type in available_movie_types:
            return movie_type
        else:
            print(
                f"Sorry, that's not a valid movie type for your age group. Please choose from {', '.join(available_movie_types)}.")


def display_recommendations(movies, movie_type):
    initial_movies = movies[:3]
    more_movies = movies[3:6]

    print(f"Based on your age and preference, here are some {movie_type} movie recommendations for you:")
    for movie in initial_movies:
        print(f"- {movie}")

    while True:
        more_movies_response = input(f"Would you like to see more {movie_type} movies? (yes/no) ").strip().lower()
        if more_movies_response == 'yes':
            print(f"Here are three more {movie_type} movie recommendations for you:")
            for movie in more_movies:
                print(f"- {movie}")
            initial_movies.extend(more_movies)
            break
        elif more_movies_response == 'no':
            break
        else:
            print("Invalid response. Please type 'yes' or 'no'.")

    return initial_movies


def select_movie(name, initial_movies):
    while True:
        movie_wanted = input(f"{name}, what specific movie do you want to watch from the recommendations? ").strip()
        if movie_wanted in initial_movies:
            print(f"Great choice! Enjoy watching '{movie_wanted}', {name}!")
            return
        else:
            print(f"Sorry, {name}. '{movie_wanted}' is not suitable for your age group or doesn't match the genre.")
            response = input(
                "Would you like to choose another movie or see recommendations for a different genre? (type 'another' to choose another movie, or 'nevermind' to see a different genre) ").strip().lower()
            if response == 'nevermind':
                return 'nevermind'
            elif response == 'another':
                continue
            else:
                print(
                    "Invalid response. Please type 'another' to choose another movie or 'nevermind' to see a different genre.")


def main():
    print("Welcome to the Movie Recommendation System!")

    name = input("What's your name? ")
    print(f"Hi {name}!")

    birth_year = get_user_birth_year()
    age = calculate_age(birth_year)
    print(f"You are {age} years old.")

    while True:
        _, _, available_movie_types = recommend_movies(age, "action")
        movie_type = get_user_movie_type(available_movie_types)

        movies, age_group, _ = recommend_movies(age, movie_type)
        initial_movies = display_recommendations(movies, movie_type)

        if select_movie(name, initial_movies) == 'nevermind':
            continue
        else:
            break


if __name__ == "__main__":
    main()
