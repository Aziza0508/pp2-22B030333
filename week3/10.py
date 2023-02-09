def has_33(nums):
    # Start at the second element, and look at indices i, i-1
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i] and nums[i] == 3:
            # found two numbers in a row equal to 3
            return True

    # no match found return false
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))