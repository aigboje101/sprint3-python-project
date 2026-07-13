# a) Extract game names into a list
game_names = []
for game in video_game_sales:
    game_names.append(game[NAME])

print(game_names)

# b) Append a new game
video_game_sales.append([21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo', 7.45, 5.21, 7.37, 31.18])
print(len(video_game_sales))

# c) Create metadata tuple
dataset_info = (len(video_game_sales), 10, 'Video Game Sales')  # QA fix: was hardcoded 20; now matches length after append (21)
