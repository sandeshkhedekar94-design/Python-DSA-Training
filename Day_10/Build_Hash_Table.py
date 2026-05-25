class MyHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        return "Not Found"


if __name__ == "__main__":

    h = MyHashTable(10)

    h.insert(1, "Apple")
    h.insert(2, "Banana")
    h.insert(12, "Orange")   

    print(h.search(1))
    print(h.search(2))
    print(h.search(12))
    print(h.search(5))