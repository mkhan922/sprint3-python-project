for sale in video_game_sales:
    if sale[GLOBAL_SALES] > 25:
        print(sale[NAME], sale[GLOBAL_SALES])
#
#
pre_2000_count = 0
for game in video_game_sales:
    if game[YEAR] < 2000:
        pre_2000_count = pre_2000_count + 1
print(pre_2000_count)
#
#

total_na_sales = 0
total_jp_sales = 0

for game in video_game_sales:
    total_na_sales = total_na_sales + game[NA_SALES]
    total_jp_sales = total_jp_sales + game[JP_SALES]

print("Total North America sales:", total_na_sales)
print("Total Japan sales:", total_jp_sales)


if total_na_sales > total_jp_sales:
    print("North American sales are higher than Japan sales")
else:
    print("Japan sales are higher than North American sales")

nintendo_games = []

for game in video_game_sales:
    if game[PUBLISHER] == 'Nintendo':
        nintendo_games.append(game[NAME])

print(nintendo_games)
print(len(nintendo_games))
