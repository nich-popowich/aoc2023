NEW_MAP_STR = 'map:'
IN_FILE = 'input_day5.txt'
with open(IN_FILE) as f:
    input_txt = f.read()
seeds = []
seeds_filtered = []
map = {}

for line_idx, line in enumerate(input_txt.splitlines() + [NEW_MAP_STR]):
    if line_idx == 0:
        seeds = [int(x) for x in line.split(':')[1].split()]
        seeds_filtered = [False]*len(seeds)
        continue
    line_split = line.split()
    if len(line_split) == 0:
        continue
    if line_split[-1] == NEW_MAP_STR:
        seeds_filtered = [False]*len(seeds)
        continue
    dest, source, length = [int(x) for x in line.split()]
    for seed_idx, seed_val in enumerate(seeds):
        if seeds_filtered[seed_idx]:
            continue
        if source <= seed_val <= source + length - 1:
            seeds[seed_idx] += dest - source
            seeds_filtered[seed_idx] = True

print(min(seeds))