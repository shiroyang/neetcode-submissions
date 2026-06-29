from collections import defaultdict
from bisect import bisect_left
class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.d[key]: self.d[key].append((0, ""))
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.d[key]: return ""
        idx = bisect_left(self.d[key], timestamp, key= lambda x:x[0]) 
        if idx < len(self.d[key]) and self.d[key][idx][0] == timestamp:
            return self.d[key][idx][1] 
        return self.d[key][idx-1][1] 

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# All the timestamps timestamp of set are strictly increasing.
# [0, 4, 6, 7] -> 5、つまり bisect_left の一つ手前を返す
# [0, 4, 6, 7] -> 4、つまり 同じ数字の場合は、その数値を返す