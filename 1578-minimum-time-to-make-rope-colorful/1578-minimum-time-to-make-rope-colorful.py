class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        counter=[neededTime[0]]
        mintime=0
        for i in range(1, len(colors)):
            if colors[i]==colors[i-1]:
                counter.append(neededTime[i])
            else:
                mintime+=sum(counter)-max(counter)
                counter=[neededTime[i]]
        mintime+=sum(counter)-max(counter)
        return mintime
       