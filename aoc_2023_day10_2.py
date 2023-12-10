IN_FILE = 'input_day10.txt'

N_CON = ['|','7','F','S']
E_CON = ['-','J','7','S']
S_CON = ['|','L','J','S']
W_CON = ['-','L','F','S']
N_IDX,E_IDX,S_IDX,W_IDX = 0,1,2,3
DIR_PT_CHANGE_MAP = [(-1,0),(0,1),(1,0),(0,-1)]
DIR_CON_MAP = [(N_CON, S_CON),(E_CON,W_CON),(S_CON,N_CON),(W_CON,E_CON)]
DIR_TURNBACK_MAP = [S_IDX,W_IDX,N_IDX,E_IDX,-1] # last idx used for init loop

def check_next_dir_valid(row_pt, col_pt, dir, max_row, max_col):
    if dir == N_IDX:
        return row_pt > 0
    if dir == E_IDX:
        return col_pt < max_col - 1
    if dir == S_IDX:
        return row_pt < max_row - 1
    return col_pt > 0

def check_next_symbol(full_map, curr_sym, row_pt, col_pt, dir, last_dir, max_row, max_col):
    if not check_next_dir_valid(row_pt, col_pt, dir, max_row, max_col):
        return False, None
    if dir == DIR_TURNBACK_MAP[last_dir]:
        return False, None
    row_change, col_change = DIR_PT_CHANGE_MAP[dir]
    dest_con, source_con = DIR_CON_MAP[dir]
    cmp_sym = full_map[row_pt+row_change][col_pt+col_change]
    if cmp_sym in dest_con and curr_sym in source_con:
        row_pt += row_change
        col_pt += col_change
        return True, cmp_sym, row_pt, col_pt, dir
    return False, None

full_map = []

with open(IN_FILE) as f:
    input_lines = f.readlines()

for row_idx, line in enumerate(input_lines):
    new_row = []
    for char in line:
        if char != '\n':
            new_row += [char, ' ']
    full_map.append(['.'] + new_row[:-1] + ['.'])
    full_map.append(['.'] + [' ' for char in new_row][:-1] + ['.'])
full_map = [['.' for char in full_map[0]]] + full_map[:-1] + [['.' for char in full_map[0]]]

# FILL IN MAP EXTENSIONS
for row_idx, row in enumerate(full_map): # First pass, only do original rows
    if row_idx % 2 == 0:
        continue
    for col_idx, val in enumerate(row):
        if val == ' ': #Extension part, fill in
            if full_map[row_idx][col_idx+1] in E_CON and full_map[row_idx][col_idx-1] in W_CON:
                full_map[row_idx][col_idx] = '-'
            else:
                full_map[row_idx][col_idx] = '.'

for row_idx, row in enumerate(full_map): # Second pass, do the rest
    for col_idx, val in enumerate(row):
        if val == ' ': #Extension part, fill in
            if full_map[row_idx-1][col_idx] in N_CON and full_map[row_idx+1][col_idx] in S_CON:
                full_map[row_idx][col_idx] = '|'
            else:
                full_map[row_idx][col_idx] = '.'

path_coords = set()
max_row = len(full_map)
max_col = len(full_map[0])

# Get start point
row_pt = 0
col_pt = 0
for row_idx, line in enumerate(full_map):
    if 'S' in line:
        row_pt = row_idx
        col_pt = line.index('S')
        break

# Get path coords
curr_sym = 'S'
last_dir = -1
while True:
    for dir in range(4):
        sym_check_out = list(check_next_symbol(full_map, curr_sym, row_pt, col_pt, dir, last_dir, max_row, max_col))
        if sym_check_out.pop(0):
            curr_sym, row_pt, col_pt, last_dir = sym_check_out
            path_coords.add((row_pt, col_pt))
            break
    if curr_sym == 'S':
        break

# Clear the non path junk
for row_idx, row in enumerate(full_map):
    for col_idx, val in enumerate(row):
        if (row_idx, col_idx) not in path_coords:
            full_map[row_idx][col_idx] = '.'

# Canvas the non isolated ground
row_pt = 0
col_pt = 0
fork_points = set()
while True:
    full_map[row_pt][col_pt] = '0'
    viable_options = []
    for dir in range(4):
        if not check_next_dir_valid(row_pt, col_pt, dir, max_row, max_col):
            continue
        row_change, col_change = DIR_PT_CHANGE_MAP[dir]
        if full_map[row_pt+row_change][col_pt+col_change] == '.':
            viable_options.append((row_pt+row_change, col_pt+col_change))
    if len(viable_options) == 0: # Go back to a fork point if possible or break
        if len(fork_points) == 0:
            break # Done canvassing
        row_pt, col_pt = fork_points.pop()
        continue
    if len(viable_options) > 1: # Add to fork_points
        fork_points.add((row_pt, col_pt))
    if len(viable_options) == 1 and (row_pt, col_pt) in fork_points: # Remove if necessary from fork points
        fork_points.remove((row_pt, col_pt))
    row_pt, col_pt = viable_options[0]

# Unexpand the map
recompressed_map = []
for row_idx in range(1, len(full_map), 2):
    recompressed_map.append(full_map[row_idx][1::2])

full_map = recompressed_map

iso_tiles = 0
for row in full_map:
    iso_tiles += row.count('.')
print(iso_tiles)
