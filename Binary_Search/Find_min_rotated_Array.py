def find_min_rotated_array(nums):
    left, right = 0, len(nums) - 1
    res = nums[0]

    while left <= right:
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break

        mid = (left + right)//2
        res = min(res, nums[mid])
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1
    return res

print(find_min_rotated_array([4,5,6,7]))