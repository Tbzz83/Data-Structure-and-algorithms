# Basic demonstration of how a hash table works, handling collisions using a chaining method
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        # This whole for loop is checking to see if there is already a key, value pair, for the key you are trying to
        # Write a new value for. If there is, the old key value pair is overwritten.
        # The enumerate function is going through the list within the arr list.
        # Inside this list are key value tuples.
        # Each tuple = element Eg. [[('march 6', 120), ('march 17', 459)]]
        # This method uses chaining
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val) # Chaining method

                # The above line here is overwriting
                # old key, value pair since tuples are immutable
                found = True
                break

        if not found:
            self.arr[h].append((key, val))


    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]




t = HashTable()

t['march 6'] = 120
t['march 6'] = 12


print(t.arr)




