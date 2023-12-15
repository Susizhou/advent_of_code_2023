import re

def sum_power_min_cubes(games):

    power_min_set_cubes = []
    for (game,value) in games.items():

        green = list(map(int,re.findall(r'(\d+) green', value)))
        red = list(map(int,re.findall(r'(\d+) red', value)))
        blue = list(map(int,re.findall(r'(\d+) blue', value)))

        power = max(green)*max(red)*max(blue)

        power_min_set_cubes.append(power)

    return sum(power_min_set_cubes)
     
 
if __name__ == '__main__':

    #12 red cubes, 13 green cubes, and 14 blue cubes

    games = {}
    with open('./advent_of_code/day_2/input.txt') as f:
        for line in f:
            (key, val) = line.split(':')
            game_nr = re.findall(r'\d+', key)[0]
            games[int(game_nr)] = val

    print(sum_power_min_cubes(games))