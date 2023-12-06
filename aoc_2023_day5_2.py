NEW_MAP_STR = 'map:'
IN_FILE = 'input_day5.txt'
with open(IN_FILE) as f:
    input_txt = f.read()
seeds = []
map = {}

import time

for line_idx, line in enumerate(input_txt.splitlines() + [NEW_MAP_STR]):
    if line_idx == 0:
        seed_nums = [int(x) for x in line.split(':')[1].split()]
        seed_bases = seed_nums[::2]
        seed_lengths = seed_nums[1::2]
        for num_idx in range(int(len(seed_nums)/2)):
            seeds.append({'base': seed_bases[num_idx], 'len': seed_lengths[num_idx], 'filt': False})
        continue

    line_split = line.split()
    if len(line_split) == 0:
        continue
    if line_split[-1] == NEW_MAP_STR: # Reset filters, refactor seed dicts in case of overlap
        seeds = sorted(seeds, key=lambda x: x['base'])
        new_seeds = [seeds[0].copy()]
        for seed_idx in range(1, len(seeds)):
            if seeds[seed_idx]['base'] == seeds[seed_idx-1]['base'] + seeds[seed_idx-1]['len']:
                new_seeds[-1]['len'] += seeds[seed_idx]['len']
            else:
                new_seeds.append(seeds[seed_idx].copy())
        seeds = new_seeds
        for seed_idx in range(len(seeds)):
            seeds[seed_idx]['filt'] = False
        continue

    map_dest_start, map_source_start, map_length = [int(x) for x in line.split()]
    
    list_segmented = True
    while list_segmented:
        list_segmented = False
        for seed_idx in range(len(seeds)):
            if seeds[seed_idx]['filt']:
                continue
            seed_start = seeds[seed_idx]['base']
            seed_end = seed_start + seeds[seed_idx]['len']
            map_source_end = map_source_start + map_length
            map_dest_end = map_dest_start + map_length

            if seed_start < map_source_start:
                if seed_end <= map_source_start: # Seeds exists entirely before map source
                    continue
                elif seed_end <= map_source_end: # Seeds start before map source and end in the map_source
                    seeds[seed_idx]['len'] = map_source_start - seed_start # Cut down unmapped seeds
                    seeds.append({'base': map_dest_start, 'len': seed_end-map_source_start, 'filt': True}) # Add freshly mapped seeds to their own dict
                    list_segmented = True
                else: # Seeds exist before and after map source
                    seeds[seed_idx]['len'] = map_source_start - seed_start # Cut down unmapped seeds
                    seeds.append({'base': map_dest_start, 'len': map_length, 'filt': True}) # Add freshly mapped seeds to their own dict
                    seeds.append({'base': map_source_end, 'len': seed_end-map_source_end, 'filt': False}) # Add leftover seeds post map source to their own dict
                    list_segmented = True
            elif seed_start < map_source_end:
                if seed_end <= map_source_end: # Seeds exist entirely within map source
                    seeds[seed_idx]['base'] += map_dest_start - map_source_start
                    seeds[seed_idx]['filt'] = True
                else: # Seeds start in map source end end after it
                    seeds[seed_idx]['base'] += map_dest_start - map_source_start
                    seeds[seed_idx]['len'] = map_source_end - seed_start
                    seeds[seed_idx]['filt'] = True
                    seeds.append({'base': map_source_end, 'len': seed_end-map_source_end, 'filt': False}) # Add leftover seeds post map source to their own dict
                    list_segmented = True

print(seeds[0]['base'])