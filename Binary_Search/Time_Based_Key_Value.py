class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key, timestamp):
        result = ""
        values = self.store.get(key, [])

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            stored_timestamp = values[mid][1]

            if stored_timestamp <= timestamp:
                result = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
            
        return result


# Test
obj = TimeMap()
obj.set("foo", "bar", 1)
print(obj.get("foo", 1))   # "bar"
print(obj.get("foo", 3))   # "bar"
obj.set("foo", "bar2", 4)
print(obj.get("foo", 4))   # "bar2"
print(obj.get("foo", 5))   # "bar2"

