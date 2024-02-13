import matplotlib.pyplot as plt

# Initialize the iterations dictionary with empty lists for each complexity
iterations = { 'O(1)': [], 'O(log n)': [], 'O(n)': [], 'O(n log n)': [], 'O(n^2)': [] }

# O(1) - Constant Time Function
def constant_time_operation(n):
    """Always performs a single operation."""
    return 1, 1

# O(log n) - Binary Search on sorted array for the last element
def binary_search_adjusted(n):
    """Performs binary search on a sorted array for the last element."""
    array = list(range(n))
    target = n - 1
    iterations = 0
    low, high = 0, len(array) - 1
    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if array[mid] == target:
            return mid, iterations
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, iterations

# O(n) - Linear Search
def linear_search(n):
    """Performs a linear search on n elements."""
    return None, n

# O(n log n) - Merge Sort
def merge_sort(arr):
    """Sorts an array using the merge sort algorithm."""
    iterations = 0  # Use a simple integer to count iterations
    
    def merge(left, right):
        nonlocal iterations
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            iterations += 1  # Count each comparison as an iteration
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        # Append the remaining elements of left and right
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def sort(sub_arr):
        nonlocal iterations
        if len(sub_arr) <= 1:
            return sub_arr
        
        mid = len(sub_arr) // 2
        left = sort(sub_arr[:mid])
        right = sort(sub_arr[mid:])
        
        # Merge the sorted halves
        return merge(left, right)
    
    sorted_arr = sort(arr)
    return sorted_arr, iterations


# O(n^2) - Bubble Sort
def bubble_sort(n):
    """Sorts n elements using bubble sort algorithm."""
    arr = list(range(n, 0, -1))
    iterations = 0
    for i in range(n):
        for j in range(n - i - 1):
            iterations += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, iterations

n_values = list(range(1, 100))
for n in n_values:
    _, it = constant_time_operation(n)
    iterations['O(1)'].append(it)
    
    _, it = binary_search_adjusted(n)
    iterations['O(log n)'].append(it)
    
    _, it = linear_search(n)
    iterations['O(n)'].append(it)
    
    _, it = merge_sort(list(range(n)))
    iterations['O(n log n)'].append(it)
    
    _, it = bubble_sort(n)
    iterations['O(n^2)'].append(it)

# Plotting
plt.figure(figsize=(12, 8))
for complexity, it_values in iterations.items():
    plt.plot(n_values, it_values, label=complexity)
plt.xlabel('n')
plt.ylabel('Iteration Count')
plt.title('Iteration Count vs. n for Different Algorithm Complexities')
plt.legend()
#plt.yscale('log', base=2)  # Using log scale for better visualization
plt.savefig(r'./complexity.png')

