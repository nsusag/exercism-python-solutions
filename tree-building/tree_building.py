class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

'''
def BuildTree(records):
    root = None
    # sorts input by record id
    records.sort(key=lambda x: x.record_id)
    # creates list of just record ids
    ordered_id = [i.record_id for i in records]
    if records:
        # negative elements count from the right, so the -1 element is the last element
        # This chunk of code makes sure ids are 0 to len(ordered_id) - 1
        if ordered_id[-1] != len(ordered_id) - 1:
            raise ValueError('Tree must be continuous')
        if ordered_id[0] != 0:
            raise ValueError('Tree must start with id 0')
    trees = []
    parent = {}
    for i in range(len(ordered_id)):
        for j in records:
            if ordered_id[i] == j.record_id:
                # fairly self explanatory error checking 
                if j.record_id == 0:
                    if j.parent_id != 0:
                        raise ValueError('Root node cannot have a parent')
                if j.record_id < j.parent_id:
                    raise ValueError('Parent id must be lower than child id')
                if j.record_id == j.parent_id:
                    if j.record_id != 0:
                        raise ValueError('Tree is a cycle')
                # if no errors, appends
                trees.append(Node(ordered_id[i]))
    for i in range(len(ordered_id)):
        for j in trees:
            if i == j.node_id:
                parent = j
        for j in records:
            if j.parent_id == i:
                for k in trees:
                    if k.node_id == 0:
                        continue
                    if j.record_id == k.node_id:
                        child = k
                        parent.children.append(child)
    if len(trees) > 0:
        root = trees[0]
    return root
'''

def BuildTree(records):
    root = None
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records] 
    if ordered_id[-1] != len(ordered_id) - 1:
        raise ValueError('Tree must be continuous')
    if ordered_id[0] != 0:
        raise ValueError('Tree must start with id 0')
    trees = []
    parent = {}
    for i in range(len(ordered_id)):
        for j in records:
            if ordered_id[i] == j.record_id:
                # fairly self explanatory error checking 
                if j.record_id == 0:
                    if j.parent_id != 0:
                        raise ValueError('Root node cannot have a parent')
                if j.record_id < j.parent_id:
                    raise ValueError('Parent id must be lower than child id')
                if j.record_id == j.parent_id:
                    if j.record_id != 0:
                        raise ValueError('Tree is a cycle')
                # if no errors, appends
                trees.append(Node(ordered_id[i]))
    for i in range(len(ordered_id)):
        for j in trees:
            if i == j.node_id:
                parent = j
        for j in records:
            if j.parent_id == i:
                for k in trees:
                    if k.node_id == 0:
                        continue
                    if j.record_id == k.node_id:
                        child = k
                        parent.children.append(child)
    if len(trees) > 0:
        root = trees[0]
    print(trees, parent)
    return root

records = [
    Record(0, 0),
    Record(1, 0),
    Record(2, 0),
    Record(3, 1),
    Record(4, 1),
    Record(5, 1),
    Record(6, 2),
]
BuildTree(records)
