class TimeMap:

    def __init__(self):
        self._map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self._map:
            return ""
        
        vals = self._map[key]
        # left part: x <= timestamp -> vals[: pos]
        pos = bisect.bisect_right(vals, timestamp, key=lambda x: x[0]) - 1
    
        if pos >= 0:
            return vals[pos][1]
        
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)