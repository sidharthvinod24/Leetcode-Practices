# Problem:
# Given an array, for each element, calculate the product of all elements except itself.

# Key Idea:
# Use prefix (product of all elements to the left of the current element).

# Use postfix (product of all elements to the right of the current element).

# Multiply prefix and postfix for each element to get the final result.

# Steps:
# Initialize a Result Array:

# Create an array of the same size as the input array, filled with 1s.

# Example: For [1, 2, 3, 4], initialize Result = [1, 1, 1, 1].

# Calculate Prefix Products:

# Traverse the array from the start to the end.

# For each element, store the product of all elements to its left in the result array.

# Use a running variable prefix to track the product.

# Example:

# After prefix calculation, Result = [1, 1, 2, 6].

# Explanation:

# For 1, no elements to the left → 1.

# For 2, prefix = 1 → 1.

# For 3, prefix = 1 * 2 = 2.

# For 4, prefix = 1 * 2 * 3 = 6.

# Calculate Postfix Products and Multiply with Prefix:

# Traverse the array from the end to the start.

# For each element, calculate the product of all elements to its right and multiply it with the corresponding value in the result array.

# Use a running variable postfix to track the product.

# Example:

# After postfix calculation, Result = [24, 12, 8, 6].

# Explanation:

# For 4, no elements to the right → 6 * 1 = 6.

# For 3, postfix = 4 → 2 * 4 = 8.

# For 2, postfix = 3 * 4 = 12 → 1 * 12 = 12.

# For 1, postfix = 2 * 3 * 4 = 24 → 1 * 24 = 24.

# Final Result:

# The result array now contains the product of all elements except the current element.

# Example: Result = [24, 12, 8, 6].

# Why This Works:
# Prefix gives the product of all elements to the left of the current element.

# Postfix gives the product of all elements to the right of the current element.

# Multiplying prefix and postfix gives the product of all elements except the current one.

# Example Walkthrough:
# Input Array: [1, 2, 3, 4]

# Prefix Products: [1, 1, 2, 6]

# Postfix Products: [24, 12, 4, 1]

# Final Result: [24, 12, 8, 6]

# Key Takeaway:
# Use prefix and postfix to avoid division and solve the problem efficiently in O(n) time.

# This method works for any array, even with zeros! 🚀


nums = [1, 2, 3, 4]
res = [1] * len(nums)

prefix = 1
for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]

postfix = 1
for i in range(len(nums)-1, -1, -1):
    res[i] *= postfix
    postfix *= nums[i]

print(res)
