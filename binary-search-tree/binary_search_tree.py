class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = None
        self.left = None
        self.right = None

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)

class BinarySearchTree:
    def __init__(self, tree_data):
        self.d = tree_data

    def data(self):
        self.sorted_data() 
        if len(self.d) == 0:
            return None
        elif len(self.d) == 1:
            return TreeNode(self.d)
        else:
            data = self.d[len(self.d) // 2]
            left = BinarySearchTree(self.d[:len(self.d) // 2]).data()
            right = BinarySearchTree(self.d[(len(self.d) // 2) + 1:]).data()
            return TreeNode(data, left, right)

    def sorted_data(self):
        newlst = [] 
        for element in self.d:
            newlst.append(int(element))
        newlst = sorted(newlst)
        for i, element in enumerate(newlst):
            newlst[i] = str(element)
        self.d = newlst
        return newlst
