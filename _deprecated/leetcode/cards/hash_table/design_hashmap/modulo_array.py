class MyHashMap:
    def __init__(self):
        self.key_range = 2069
        self.hash_table = [Bucket() for i in range(self.key_range)]

    def _hash(self, key):
        return key % self.key_range

    def put(self, key, value):
        hash_key = self._hash(key)
        self.hash_table[hash_key].update(key, value)

    def get(self, key):
        hash_key = self._hash(key)
        return self.hash_table[hash_key].get(key)

    def remove(self, key):
        hash_key = self._hash(key)
        self.hash_table[hash_key].remove(key)

    def print_buckets(self):
        for hash_table in self.hash_table:
            hash_table.display()


class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for k, v in self.bucket:
            if k == key:
                return v
        return -1

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        if not found:
            self.bucket.append((key, value))

    def display(self):
        for k, bucket in self.bucket:
            if bucket:
                print(bucket)


obj = MyHashMap()
obj.put(1, "A")
obj.put(2, "B")
obj.put(3, "C")
obj.put(4, "D")
obj.put(5, "E")
obj.remove(2)
print(f"Value if key 3 is {obj.get(3)}.")
print(f"Value if key 2 is {obj.get(2)}.")
obj.print_buckets()
"""
Output:
Value if key 3 is C.
Value if key 2 is -1.
A
C
D
E

Time complexity: for each of the methods, the time complexity is O(N/K) where N is the number of all possible keys and
K is the number 
of predefined buckets in the hashmap, which is 2069 in our case.
Space Complexity: O(K+M) where K is the number of predefined buckets in the hashmap and M is the number of unique keys 
that have been inserted into the hashmap.
"""
