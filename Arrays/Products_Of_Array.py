#
# ! Approach: Fill out the the i + n, with nums[i]
# * Space - O(n)
# * Time - O(n)

def Solution(nums):
        # nums = [1,2,4,6]
        n = len(nums)
        res = [1] * n #[1,1,1,1]

        prefix = 1
        for i in range(n):
            res[i] = prefix 
            # res[0] = 1
            # res[1] = 1
            # res[2] = 2
            # res[3] = 8
            prefix *= nums[i]
            # 1 * 1 = 1 ( Now prefix become)
            # 1 * 2 = 2 ( prefix )
            # 2 * 4 = 8
            # 8 * 6 = 48
            # Now res becomes  res = [1,1,2,8]

        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            # res[3] = 8 * 1 = 8
            # res[2] = 2 * 6 = 12
            # res[1] = 1 * 24 = 24
            # res[0] = 1 * 48 = 48. 
            suffix *= nums[i]
            # 1 * 6 = 6
            # 6 * 4 = 24
            # 24 * 2 = 48
            # 48 * 1 = 48

        return res # [48,24,12,8]


print(Solution([1,2,4,6]))