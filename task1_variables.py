# a) Total number of games
total_games = len(video_game_sales)
print(total_games)

# b) Average global sales
total_sales = 0
for game in video_game_sales:
    total_sales = total_sales + game[GLOBAL_SALES]

avg_global_sales = total_sales / len(video_game_sales)
print(f"Average global sales: {avg_global_sales}")

# c) Top game's share of total sales
top_game_share = (video_game_sales[0][GLOBAL_SALES] / total_sales) * 100
print(top_game_share)
