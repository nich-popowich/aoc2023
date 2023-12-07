IN_FILE = 'input_day7.txt'
MAX_SCORE = 6
CHAR_MAP = [('A','e'), ('K','d'), ('Q','c'), ('J','b'), ('T','a')]

def check_match(hand):
    match_list = []
    for card in set(hand):
        hand_sel_card_only = hand
        for comp_card in set(hand):
            if comp_card != card:
                hand_sel_card_only = hand_sel_card_only.replace(comp_card, '')
        match_list.append(len(hand_sel_card_only))

    score = max(match_list) # returns 1,2,3,4 or 5
    o_score = score
    if score >= 4 or set(match_list) == {2,3}:
        score += 1 # Add 1 to account for Full House -> 4, 5 become 5,6, full house becomes 4
    elif match_list.count(1) >= 3:
        score -= 1 # Subtract 1 to account for Two Pair -> One pair becomes 1, high card becomes 0
    return score
        
def sort_hand(hand_list):
    hand_list_translated = []
    for hand, bid in hand_list:
        hand_translated = hand
        for char_in, char_out in CHAR_MAP:
            hand_translated = hand_translated.replace(char_in, char_out)
        hand_translated = int('0x' + hand_translated, 16)
        hand_list_translated.append((hand, hand_translated, bid))
    hand_list_translated = sorted(hand_list_translated, key=lambda x: x[1])
    return [(x[0], x[2]) for x in hand_list_translated]

with open(IN_FILE) as f:
    type_lists = [[] for __ in range(MAX_SCORE+1)]
    for line in f.readlines():
        hand, bid = line.split()

        hand_type = check_match(hand)
        type_lists[hand_type].append((hand, bid))
rank = 1
final_num = 0
for type_list in type_lists:
    for hand, bid in sort_hand(type_list):
        final_num += int(bid)*rank
        rank += 1
print(final_num)
