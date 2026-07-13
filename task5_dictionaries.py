# a) Total global sales by genre
sales_by_genre = {}
for game in video_game_sales:
    genre = game[GENRE]
    if genre in sales_by_genre:
        sales_by_genre[genre] = sales_by_genre[genre] + game[GLOBAL_SALES]
    else:
        sales_by_genre[genre] = game[GLOBAL_SALES]

print(sales_by_genre)

# b) Game count per publisher
games_per_publisher = {}
for game in video_game_sales:
    publisher = game[PUBLISHER]
    if publisher in games_per_publisher:
        games_per_publisher[publisher] = games_per_publisher[publisher] + 1
    else:
        games_per_publisher[publisher] = 1

print(games_per_publisher)

# c) Top game dictionary
top_game = {
    'name': video_game_sales[0][NAME],
    'year': video_game_sales[0][YEAR],
    'genre': video_game_sales[0][GENRE],
    'publisher': video_game_sales[0][PUBLISHER],
    'global_sales': video_game_sales[0][GLOBAL_SALES]
}

for key, value in top_game.items():
    print(f"{key}: {value}")
