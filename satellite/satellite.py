def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("The pre-order traversal is not equal in length to the in-order traversal.")
    for i, element in enumerate(preorder):
        if element not in inorder:
            raise ValueError("The pre-order and in-order traversals do not contain the same elements.") 
        if preorder.index(element) != i:
            raise ValueError("There exists a repeated element in the pre-order traversal or in-order traversal.")
    tree = {}
    if len(preorder) == 0:
        return tree
    tree["v"] = preorder[0]    
    startofright = inorder.index(preorder[0])   
    tree["l"] = tree_from_traversals(preorder[1:startofright + 1], inorder[0:startofright])
    tree["r"] = tree_from_traversals(preorder[startofright + 1:], inorder[startofright + 1:])
    return tree
