
# * Input: height = [0,2,0,3,1,0,1,3,2,1]
# * Output: 9

def rainWaterTapping(height):
    l, r = 0, len(height) - 1
    water = 0
    leftMax, rightMax = 0, 0 

    while l < r:
        if height[l] <= height[r]:
            leftMax = max(height[l], leftMax)
            water += leftMax - height[l]
            l += 1
        else:
            rightMax = max(height[r], rightMax)
            water += rightMax - height[r]
            r -= 1
    return water

print(rainWaterTapping([0,2,0,3,1,0,1,3,2,1]))