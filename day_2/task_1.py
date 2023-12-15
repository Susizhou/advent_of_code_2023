import re

def possible_games_sum(games):

    possible_games_id = []
    for (game,value) in games.items():

        green = list(map(int,re.findall(r'(\d+) green', value)))
        red = list(map(int,re.findall(r'(\d+) red', value)))
        blue = list(map(int,re.findall(r'(\d+) blue', value)))

        if max(green) <= 13 and max(red) <= 12 and max(blue) <= 14:
            possible_games_id.append(game)

    return sum(possible_games_id)
     
 
if __name__ == '__main__':

    #12 red cubes, 13 green cubes, and 14 blue cubes

    games = {}
    with open('./advent_of_code/day_2/input.txt') as f:
        for line in f:
            (key, val) = line.split(':')
            game_nr = re.findall(r'\d+', key)[0]
            games[int(game_nr)] = val

    print(possible_games_sum(games))