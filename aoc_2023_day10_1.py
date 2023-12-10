IN_FILE = 'input_day10.txt'

import time

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

import time

full_map = []
row_pt = 0
col_pt = 0
with open(IN_FILE) as f:
    input_lines = f.readlines()

max_row = len(input_lines)
max_col = len(input_lines[0])

for row_idx, line in enumerate(input_lines):
    full_map.append([char for char in line])
    if 'S' in line:
        row_pt = row_idx
        col_pt = line.find('S')

loop_length = 0
curr_sym = 'S'
last_dir = -1

while True:
    for dir in range(4):
        sym_check_out = list(check_next_symbol(full_map, curr_sym, row_pt, col_pt, dir, last_dir, max_row, max_col))
        if sym_check_out.pop(0):
            curr_sym, row_pt, col_pt, last_dir = sym_check_out
            loop_length += 1
            break
    if curr_sym == 'S':
        break

print(int(loop_length/2))
