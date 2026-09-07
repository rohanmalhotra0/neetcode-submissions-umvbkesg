class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        Reached = Counter()
        uniqueTimes = set()
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            
            if time not in uniqueTimes:
                uniqueTimes.add(time)
        return len(uniqueTimes)

