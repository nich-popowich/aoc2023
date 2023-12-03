MAX_DICT = {'red': 12, 'green': 13, 'blue': 14}
IN_FILE = 'input_day2.txt'

final_num = 0
with open(IN_FILE) as f:
    for line in f.readlines():
        game_id = int(line.split(':')[0].replace('Game ', ''))
        max_colour_dict = {'red': 0, 'green': 0, 'blue': 0}
        cube_sets = line.split(':')[1].split(';')
        for cube_set in cube_sets:
            num_colour_pairs = cube_set.split(',')
            for pair in num_colour_pairs:
                num = int(pair.split()[0])
                colour = pair.split()[1]
                max_colour_dict[colour] = max(max_colour_dict[colour], num)
        final_num += max_colour_dict['red']*max_colour_dict['green']*max_colour_dict['blue']
print(final_num)
