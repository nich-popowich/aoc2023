MAX_DICT = {'red': 12, 'green': 13, 'blue': 14}
IN_FILE = 'input_day2.txt'

final_num = 0
with open(IN_FILE) as f:
    for line in f.readlines():
        game_id = int(line.split(':')[0].replace('Game ', ''))
        valid_game = True
        cube_sets = line.split(':')[1].split(';')
        for cube_set in cube_sets:
            num_colour_pairs = cube_set.split(',')
            for pair in num_colour_pairs:
                num = int(pair.split()[0])
                colour = pair.split()[1]
                if num > MAX_DICT[colour]:
                    valid_game = False
                    break
            if not valid_game:
                break
        if valid_game:
            final_num += game_id
print(final_num)
