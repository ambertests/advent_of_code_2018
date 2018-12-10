source = open('input/input08.txt').read()
test_source = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
node_array = [int(n.strip()) for n in 
                    source.split(' ')]

#2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
# A----------------------------------
#     B----------- C-----------
#                      D-----
def add_metadata(nodes, sum_md):
    child_count = nodes[0]
    meta_count = nodes[1]
    nodes = nodes[2:]
    child_values = []
    for n in range(child_count):
        nodes, sum_md, node_val = add_metadata(nodes, sum_md)
        child_values.append(node_val)

    node_val = 0
    for m in range(meta_count):
        sum_md += nodes[m]
        if child_count == 0: 
            node_val += nodes[m]
        elif nodes[m] - 1 in range(child_count):
            node_val += child_values[nodes[m] - 1]
    

    return nodes[meta_count:], sum_md, node_val
    

    
nodes, sum_md, node_val = add_metadata(node_array, 0)
print('Solution 8.1:', sum_md)
print('Solution 8.2:', node_val)
