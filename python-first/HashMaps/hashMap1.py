class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.map = [None] * size

    def _hash(self, key):

        return hash(key) % self.size

    def add(self, key, value):
        index = self._hash(key)
        print("this the index " + str(index))
        if self.map[index] is None:
            self.map[index] = []
        self.map[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        
        if self.map[index] is not None:
            for k, v in self.map[index]:
                if k == key:
                    return v
        raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        if self.map[index] is not None:
            for i, (k, v) in enumerate(self.map[index]):
                if k == key:
                    del self.map[index][i]
                    return
        raise KeyError(key)

# Example usage
my_map = HashMap()
my_map.add("apple", 5)
my_map.add("banana", 10)
print(my_map.get("apple"))  # Output: 5
my_map.remove("apple")
# print(my_map.get("apple"))  # Raises KeyError
