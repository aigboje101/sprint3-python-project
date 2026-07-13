# a) Extract "Pokemon" from game name
game_name = video_game_sales[4][NAME]
print(game_name[:7])

# b) Clean messy names
for name in messy_names:
    print(name.strip().lower())

# c) Formatted f-string
game = video_game_sales[0]
print(f"#1 Best Seller: {game[NAME]} ({game[YEAR]}) - ${game[GLOBAL_SALES]}M global sales")
