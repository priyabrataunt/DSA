# 
# ! Concatenation of Array

# * You are given an integer array nums of length n. Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# * Specifically, ans is the concatenation of two nums arrays.

# TODO:Example 1:
# ? Input: nums = [1,4,1,2]
# ? Output: [1,4,1,2,1,4,1,2]

# TODO:Example 2:
# ? Input: nums = [22,21,20,1]
# ? Output: [22,21,20,1,22,21,20,1]

# ! Approach: Fill out the the i + n, with nums[i]
# Space - O(n)
# Time - O(n)

# * Code:

def concatenation(nums):
    n = len(nums)
    # As the new array would be 2x the nums.
    ans = [0] * (2 * n)

    for i in range(n):
        ans[i] = nums[i]
        ans[i + n] = nums[i]
    return ans

if __name__ == "__main__":
    nums = eval(input("Enter the Arrray (e.g [1,4,1,2]): "))
    print(f"Output:{concatenation(nums)}")