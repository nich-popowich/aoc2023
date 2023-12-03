IN_FILE = 'input_day3.txt'
GEAR = '*'
MAX_GEAR_RATIO_NUM = 2
with open(IN_FILE) as f:
    input_str = f.read()
symbols = set(input_str)
for char in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '\n'}:
    if char in symbols:
        symbols.remove(char)

gear_locations = []
for row_idx, row in enumerate(input_str.splitlines()):
    for col_idx, char in enumerate(row):
        if char == GEAR:
            gear_locations.append((row_idx, col_idx))

number_locations = []
for row_idx, row in enumerate(input_str.splitlines()):

    row_conditioned = row.replace('.', ' ')
    for sym in symbols:
         row_conditioned = row_conditioned.replace(sym, ' ')

    num_strs = row_conditioned.split()
    
    start_idx = 0
    for num in num_strs:

        col_idx = row.find(num, start_idx)
        start_idx = col_idx + len(num)
        number_locations.append((num, row_idx, col_idx))

final_num = 0

for gear_row_idx, gear_col_idx in gear_locations:
    ratio_buffer = []

    for num, num_row_idx, num_col_start_idx in number_locations:
        num_col_end_idx = num_col_start_idx + len(num) - 1
        
        if num_col_start_idx - 1 <= gear_col_idx <= num_col_end_idx + 1 and \
            num_row_idx - 1 <= gear_row_idx <= num_row_idx + 1:
            ratio_buffer.append(num)

    if len(ratio_buffer) == MAX_GEAR_RATIO_NUM:
        final_num += int(ratio_buffer[0])*int(ratio_buffer[1])

print(final_num)