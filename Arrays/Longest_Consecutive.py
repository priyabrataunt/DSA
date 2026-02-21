# 
# ! Longest Consecutive Sequence

'''Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.'''

# * Example:
# ? Nums = [2,20, 4, 10, 3, 4, 5]
# ** Output - 4

def LongestConsecutive(nums):
    numSet = set(nums) # numSet = [2,20, 4, 10, 3, 4, 5]
    longest = 0
    
    for n in numSet: # n = 2, 20
        if (n-1) not in numSet:
            # Then this cant be the beginning number must move to end
            # 2 - 1 = 1 "V"
            length = 1
            while(n + length) in numSet: 
                # 2 + 1 = 3 "V" 
                # 2 + 2 = 4 "V"
                # 2 + 3 = 5 "v"
                # 2 + 4 = 6 "X"
                length += 1 # Length = 2, 3, 4  ----- Here Length = 4
            longest = max(length, longest)
            # (4,0) = 4
            # Here loop then runs for the 20 ---> checks 20 -1 = 19 "X"... and so on.
            # Lastly the Longest has the 4 in it.
            # So when compared to other the 4 is the highest
            # Hence it will print as Longest = 4
    return longest


print(LongestConsecutive([2,20, 4, 10, 3, 4, 5]))        
print(LongestConsecutive([0,3,2,5,4,6,1,1]))        
