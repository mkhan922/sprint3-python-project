game_names= []
for game in video_game_sales:
    game_names.append(game[1])
print(game_names)

video_game_sales.append([21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo', 7.45, 5.21, 7.37, 31.18])
print(len(video_game_sales))

dataset_info= [21, 10, 'Video Game Sales']
dataset_info = tuple(dataset_info)
#A tuple is more appropriate because these are values that we are not wanting to change. 
print(dataset_info)
