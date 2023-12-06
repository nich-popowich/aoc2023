IN_FILE = 'input_day6.txt'
with open(IN_FILE) as f:
    input_txt = f.read()
times, records = [x.split(':')[1].split() for x in input_txt.splitlines()]

final_num = 1
for race_idx in range(len(times)):
    ways_to_win = 0
    total_time = int(times[race_idx])
    for hold_time in range(1, total_time): # ignores first/last case which give 0
        if hold_time*(total_time-hold_time) > int(records[race_idx]):
            ways_to_win += 1
    final_num *= ways_to_win
print(final_num)
