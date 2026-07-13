# a) Calculate total regional sales
def calculate_total_sales(game):
    return game[NA_SALES] + game[EU_SALES] + game[JP_SALES]

print(calculate_total_sales(video_game_sales[0]))

# b) Filter by genre with default argument
def filter_by_genre(data, genre='Platform'):
    result = []
    for game in data:
        if game[GENRE] == genre:
            result.append(game)
    return result

# Test with default
platform_games = filter_by_genre(video_game_sales)
print(f"Platform games: {len(platform_games)}")

# Test with specified genre
sports_games = filter_by_genre(video_game_sales, 'Sports')
print(f"Sports games: {len(sports_games)}")

# c) Summary function used in a loop
def get_summary(game):
    return f"{game[NAME]} ({game[YEAR]}) - {game[GENRE]} - ${game[GLOBAL_SALES]}M"

for game in video_game_sales:
    print(get_summary(game))
