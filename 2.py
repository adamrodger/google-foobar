# approach: 
# build a tree using recursion - keep splitting elements until you've only got one left
# traverse the tree to find targets, then unwind one, collecting results

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
    
    def __str__(self):
        return "%d: [left: %s, right: %s]" % (self.data, self.left, self.right)
        

def build_tree(numbers):
    node = Node(numbers[-1])
    radix = int((len(numbers) - 1) / 2)
    
    if radix == 0:
        # no more child nodes
        return node
    
    node.left = build_tree(numbers[0:radix])
    node.right = build_tree(numbers[radix:-1])
    return node

def find_parent(node, parent, target):
    if node == None:
        return -1
        
    if node.data == target:
        return -1 if parent == None else parent.data
    
    found_left = find_parent(node.left, node, target)
    if found_left > 0:
        return found_left
    
    found_right = find_parent(node.right, node, target)
    if found_right > 0:
        return found_right
        
    # not found - magic number
    return -1

def solution(h, q):
    numbers = list(range(1, 2**h))
    root = build_tree(numbers)
    results = []
    
    # bit naive because we'll recurse the tree for each target instead
    # of collecting as we recurse
    for target in q:
        parent = find_parent(root, None, target)
        results.append(parent)
        
    return results
    
if __name__ == "__main__":
    print(solution(3, [7, 3, 5, 1]))