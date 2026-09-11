class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = collections.deque([(timestamp, value)])
            return

        values = self.hashmap[key]
        values.append((timestamp, value))
        # if timestamp <= values[0][0]:
        #     values.appendleft((timestamp, value), 0)
        #     return
        # elif timestamp >= values[-1][0]:
        #     values.append((timestamp, value))
        #     return

        # l, r = 0, len(values) - 2
        # pos = -1
        # while l <= r:
        #     mid = l + (r - l) // 2
        #     if mid < len(values) - 1:
        #         if values[mid][0] <= timestamp < values[mid + 1][0]:
        #             pos = mid + 1
        #         elif values[mid][0] > timestamp:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        # values.insert(pos, (timestamp, value))        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        values = self.hashmap[key]
        if timestamp < values[0][0]:
            return ""
        elif timestamp >= values[-1][0]:
            return values[-1][1]

        l, r = 0, len(values) - 2
        while l <= r:
            mid = l + (r - l) // 2
            if mid < len(values) - 1:
                if values[mid][0] <= timestamp < values[mid + 1][0]:
                    return values[mid][1]
                elif values[mid][0] > timestamp:
                    r = mid - 1
                else:
                    l = mid + 1
        return ""
