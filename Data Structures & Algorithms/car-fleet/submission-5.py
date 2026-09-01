class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        fleets = {}
        
        for p, s in zip(position, speed):
            time.append((p, s))
        time.sort(reverse=True)

        for i, (p, s) in enumerate(time):
            time[i] = (target - p) / s
        
        stack = [time[0]]
        fleets = 0
        for t in time[1:]:
            if stack and stack[-1] < t:
                fleets += 1
                stack = []
                stack.append(t)
            
        if stack:
            fleets += 1
        return fleets
