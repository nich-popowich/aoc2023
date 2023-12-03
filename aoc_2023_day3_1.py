IN_FILE = 'input_day3.txt'

with open(IN_FILE) as f:
    input_str = f.read()
symbols = set(input_str)
for char in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '\n'}:
    if char in symbols:
        symbols.remove(char)

symbol_locations = []
for row_idx, row in enumerate(input_str.splitlines()):
    for col_idx, char in enumerate(row):
        if char in symbols:
            symbol_locations.append((char, row_idx, col_idx))

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
for num, num_row_idx, num_col_start_idx in number_locations:

    num_col_end_idx = num_col_start_idx + len(num) - 1

    for sym, sym_row_idx, sym_col_idx in symbol_locations:
        if sym_row_idx < num_row_idx - 1:
            continue
        elif sym_row_idx > num_row_idx + 1:
            break
        if num_col_start_idx - 1 <= sym_col_idx <= num_col_end_idx + 1:
            final_num += int(num)

print(final_num)