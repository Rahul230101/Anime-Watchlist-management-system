import random

anime_list = [['naruto', 'dragon ball Z', 'bleach', 'black clover', 'ranking og kings'],
              ['i want to eat your pancreas', 'silent voice', 'violet evergarden']]


while True:
    genre = input("wanna watch movies or series : ")
    if genre == 'series':
        anime_series = random.choice(anime_list[0])
        print(f"You should watch {anime_series}")
        with open("watchlist.txt", 'a') as watch_list:
            watch_list.write(f"{anime_series}\n")
        anime_list[0].remove(anime_series)

    elif genre == 'movies':
        anime_movie = random.choice(anime_list[1])
        print(f"You should watch {anime_movie}")
        with open("watchlist.txt", 'a') as watch_list:
            watch_list.write(f"{anime_movie}\n")
        anime_list[1].remove(anime_movie)
    print()
    print("series")
    print()
    for series in anime_list[0]:
        print(series)
    print()
    print("Movies")
    print()
    for movie in anime_list[1]:
        print(movie)

    ask = input("Want to search again: ")
    if ask == "yes":
        continue
    else:
        break



