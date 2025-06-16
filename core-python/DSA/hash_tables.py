from collections import deque


class LogCache:
    def __init__(self, count):
        self.count = count
        self.table = [deque() for _ in range(count)]

    def hash_function(self, key):
        return sum(ord(el) for el in key) % self.count

    def put(self, log_id, description):
        index = self.hash_function(log_id)

        for i, (existing_id, _) in enumerate(self.table[index]):
            if existing_id == log_id:
                del self.table[index][i]
                break
        self.table[index].append((log_id, description))

    def get(self, log_id):
        index = self.hash_function(log_id)
        for existing_id, description in self.table[index]:
            if existing_id == log_id:
                return description
        return None

    def remove(self, log_id):
        index = self.hash_function(log_id)
        for i, (existing_id, _) in enumerate(self.table[index]):
            if existing_id == log_id:
                del self.table[index][i]
                return True
        return False

    def keys(self):
        return [log_id for deq in self.table for log_id, _ in deq]


if __name__ == "__main__":
    cache = LogCache(5)
    cache.put("log_1", "Warning")
    cache.put("log_2", "Error")
    cache.put("log_2", "New_Error")
    print(cache.get("log_2"))
    print(cache.keys())
    print(cache.remove("log_1"))
    print(cache.keys())
