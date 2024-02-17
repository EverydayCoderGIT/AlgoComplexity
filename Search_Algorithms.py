# O(1) - Constant Time Function
def hashing_indexing_access(target_array, index):
    return target_array[index]

# O(n) - Linear Search
def linear_search(input_list, target_value):
    """Performs a linear search on n elements."""
    for index, value in enumerate(input_list):
        if value == target_value:
            return index

# O(log n) - Binary Search on sorted array for the last element
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    global iterations

    # Base Cases: root is null or key is present at root
    if root is None or root.value == key:
        return True

    iterations += 1

    # Key is greater than root's key
    if root.value < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)

# List of keys to create BST
keys = [70,4,6,90,75,2,95,98]

# Creating the BST
root = None
for key in keys:
    root = insert(root, key)

# define and initialize iterations
global iterations
iterations = 0

# Now, search for a specific key
search(root, 98)

print(f"number of iterations : {iterations}")
