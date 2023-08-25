# Define a function to perform binary search
def binary_search(list, target):
  # Set the initial low and high indices
  low = 0
  high = len(list) - 1

  # Loop until low is greater than high
  while low <= high:
    # Find the middle index
    mid = (low + high) // 2
    # Compare the middle element with the target
    if list[mid] == target:
      # Return the index if found
      return mid
    elif list[mid] < target:
      # Set the low index to mid + 1 if target is larger
      low = mid + 1
    else:
      # Set the high index to mid - 1 if target is smaller
      high = mid - 1
  
  # Return -1 if not found
  return -1

# Test the function with an example list and target
list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 14

# Print the result
result = binary_search(list, target)
if result != -1:
  print(f"Target {target} found at index {result}")
else:
  print(f"Target {target} not found in the list")
