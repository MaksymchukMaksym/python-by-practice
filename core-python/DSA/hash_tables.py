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
                self.table[index].pop(i)
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
                self.table[index].pop(i)
                return True
        return False
