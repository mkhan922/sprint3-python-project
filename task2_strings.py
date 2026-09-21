messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']
game_name = video_game_sales[4][1]
print(game_name[0:7])

for name in messy_names:
    cleaned_name = name.strip().lower()
    print(cleaned_name)

Wii = video_game_sales[0]
print(f"#{Wii[RANK]} Best Seller: {Wii[NAME]} ({Wii[YEAR]}) - ${Wii[GLOBAL_SALES]}M global sales")
