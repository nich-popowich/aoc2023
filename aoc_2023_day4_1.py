IN_FILE = 'input_day4.txt'
with open(IN_FILE) as f:
    final_num = 0
    for line in f.readlines():
        w_nums, c_nums = [x.split() for x in line.split(':')[1].split('|')]
        w_nums, c_nums = [set(x) for x in (w_nums, c_nums)]
        v_nums = c_nums.intersection(w_nums)
        final_num += 2**(len(v_nums)-1) if len(v_nums) > 0 else 0
    print(final_num)