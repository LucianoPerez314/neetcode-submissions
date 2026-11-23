class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # stack represents cars in the car fleet.
        stack = [(position[i], speed[i]) for i in range(len(position))]
        stack.sort(key=lambda x: x[0])

        # xf = xi + v * dt
        # (xf - xi) / v = dt
        # start at the end of the car fleet and work backwards 
        res = 1
        curr_fleet = stack.pop()
        duration = (target - curr_fleet[0]) / curr_fleet[1]
        while len(stack) != 0:
            curr = stack.pop()
            xi, v = curr
            dt = (target - xi) / v
            if dt <= duration: # if car can catch up to the current fleet, continue
                continue

            # otherwise, create a new fleet
            curr_fleet = curr
            duration = dt
            res += 1
        return res


        