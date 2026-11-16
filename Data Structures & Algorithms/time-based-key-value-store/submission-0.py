class TimeMap:

    def __init__(self):
        self.table = {} # key -> [(timestamp, value),...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = []
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.table.get(key, [])
        res = ""
        left = 0
        right = len(pairs) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res

