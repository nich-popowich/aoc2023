IN_FILE = 'input_day6.txt'
with open(IN_FILE) as f:
    input_txt = f.read()
total_time, record = [int(x.split(':')[1].replace(' ', '')) for x in input_txt.splitlines()]

ways_to_win = 0
first_win = total_time
last_win = 0
for hold_time in range(1, total_time): # ignores first/last case which give 0
    if hold_time*(total_time-hold_time) > record:
        first_win = hold_time
        break
for hold_time in range(total_time-1, 0, -1): # ignores first/last case which give 0
    if hold_time*(total_time-hold_time) > record:
        last_win = hold_time
        break
print(last_win-first_win+1)
