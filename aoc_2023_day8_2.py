import math
IN_FILE = 'input_day8.txt'
START_NODE_END = 'A'
DEST_NODE_END = 'Z'

node_map = {}
nodes_to_track = []
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
        if key[2] == START_NODE_END:
            nodes_to_track.append(key)

steps_to_get_to_end = [0]*len(nodes_to_track)
for idx, node in enumerate(nodes_to_track):
    steps = 0
    current_node = node
    while current_node[2] != DEST_NODE_END:
        current_node = node_map[current_node][int(directions[steps%len(directions)])]
        steps += 1
    steps_to_get_to_end[idx] = steps
print(math.lcm(*steps_to_get_to_end))

    