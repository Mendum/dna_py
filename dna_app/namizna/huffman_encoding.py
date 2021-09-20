import os
import json
import hashlib
import re

#Source code:
#https://www.programiz.com/dsa/huffman-coding

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d

# Calculating frequency
def calculate_frequency(user_input):
    freq = {}
    for c in user_input:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    nodes = freq

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    save_huffman_code_tree(huffman_code_tree(nodes[0][0]))
    return freq, huffman_code_tree(nodes[0][0])

def save_huffman_code_tree(tree):
    huffman_tree_key = hashlib.md5(json.dumps(tree).encode('utf-8')).hexdigest()
    obj = { "key" : huffman_tree_key, "tree" : tree}

    with open(os.path.join(os.getcwd(), 'db_huffman_trees.txt'), 'a') as file:
        file.write(json.dumps(obj)+"\n")

        
def read_huffman_code_tree():
    json_objects = []

    with open(os.path.join(os.getcwd(), 'db_huffman_trees.txt')) as file:
        for line in file:
            json_objects.append(json.loads(line))

    return json_objects

def encode_binary_value(user_input):
    frequency, huffmanCode = calculate_frequency(user_input)
    value = ''

    for element in user_input: 
        value+=huffmanCode[element]+' '

    return value
    
def encode_sequence_value(user_input):
    value = encode_binary_value(user_input)

def decode_biti_to_string(key, biti):
    db_trees = read_huffman_code_tree()
    value = ''
    huffman_tree = {}
    
    for tree in db_trees:
        if(tree['key'] == key):
            huffman_tree = tree['tree']

    if huffman_tree:

        key_list = list(huffman_tree.keys())
        val_list = list(huffman_tree.values())
        byte_values = re.findall(r'\S+', biti)

        for i in byte_values:
            position = val_list.index(i)
            value+=key_list[position]
        return value
    else:
        return 'Invalid key'

#binari = encode_binary_value('message')
#decoded = decode_biti_to_string('33d57e9046e53ae37b8df3cfa2d3479d', binari)
#print(decoded)