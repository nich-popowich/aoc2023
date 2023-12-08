IN_FILE = 'input_day8.txt'
START_NODE = 'AAA'
DEST_NODE = 'ZZZ'

node_map = {}
directions = ''
with open(IN_FILE) as f:
    for idx, line in enumerate(f.readlines()):
        if idx == 0:
            directions = line.strip().replace('L','0').replace('R','1')
            continue
        elif idx == 1:
            continue
        key = line.split('=')[0].strip()
        nodes = line.split('=')[1].replace('(', '').replace(')', '').replace(',', '').split()
        node_map[key] = nodes

steps = 0
current_node = START_NODE
while current_node != DEST_NODE:
    current_node = node_map[current_node][int(directions[steps%len(directions)])]
    steps += 1
print(steps)
    