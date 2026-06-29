class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n order by position asc
        # the last car will not fleet
        # n-1 -th car will only be able to fleet into n-th car
        pair = [(p, s) for p, s in zip(position, speed)]
        pair = sorted(pair, key=lambda x:-x[0])
        que = []
        for p, s in pair:
            t = (target-p) / s
            que.append(t)
            if len(que) > 1 and que[-1] <= que[-2]:
                que.pop()
        return len(que)