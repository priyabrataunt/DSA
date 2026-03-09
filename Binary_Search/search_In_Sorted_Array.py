def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:  # Left half is sorted
            if target >= nums[left] and target <= nums[mid]:
                right = mid - 1  # Search left half
            else:
                left = mid + 1   # Search right half
        else:  # Right half is sorted
            if target >= nums[mid] and target <= nums[right]:
                left = mid + 1   # Search right half
            else:
                right = mid - 1  # Search left half
    
    return -1  # Target not found


print(search([4, 5, 6, 7, 1, 2, 3], 1))