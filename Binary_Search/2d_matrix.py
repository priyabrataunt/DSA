def targetFinding(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0]) #Because we can count the number of element in the first row

    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2

        r = mid // cols
        c = mid % cols

        if matrix[r][c] == target:
            print((r, c))
            return True 
        elif matrix[r][c] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return False

print(targetFinding([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10))