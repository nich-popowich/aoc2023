IN_FILE = 'input_day4.txt'
with open(IN_FILE) as f:
    input_str_lines = f.readlines()
    max_card_num = len(input_str_lines)
    card_list = [0] * max_card_num
    for card_idx, line in enumerate(input_str_lines):
        card_list[card_idx] += 1
        w_nums, c_nums = [x.split() for x in line.split(':')[1].split('|')]
        w_nums, c_nums = [set(x) for x in (w_nums, c_nums)]
        v_nums = c_nums.intersection(w_nums)
        for n_card_idx in range(card_idx + 1, card_idx + 1 + len(v_nums)):
            if n_card_idx >= max_card_num:
                break
            card_list[n_card_idx] += card_list[card_idx]
    print(sum(card_list))