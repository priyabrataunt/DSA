from typing import List


def carFleet(target, position, speed):
        
        # Step 1: Pair position and speed
        cars = list(zip(position, speed))
        # Example:
        # position = [1,4]
        # speed = [3,2]
        # cars = [(1,3), (4,2)]
        
        # Step 2: Sort by position descending
        cars.sort(reverse=True)
        # cars becomes [(4,2), (1,3)]
        
        stack = []
        
        # Step 3: Process each car
        for pos, spd in cars:
            
            # Calculate time to reach target
            time = (target - pos) / spd
            
            # Example:
            # For (4,2): time = (10-4)/2 = 3
            # For (1,3): time = (10-1)/3 = 3
            
            # If stack empty OR this car arrives later
            # it forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
                # stack = [3]
            
            # Else:
            # If time <= stack[-1]
            # It joins the fleet ahead
            # So we do nothing
        
        # Number of fleets = size of stack
        return len(stack)
        
        
print(carFleet(10, [1,4], [3,2]))
