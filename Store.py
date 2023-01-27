# Creating a store class that stores values in a list with some minimal functionality

class Store:
    def __init__(self):
        self.values = []

    def insert(self, value):
        if value in self.values:
            return

        else:
            self.values.append(value)
        return self.values

    def remove(self, value):
        value_index = self.values.index(value)
        self.values[value_index] = self.values[-1]
        self.values.pop(-1)
        self.values.sort()
        return self.values

    def get_random(self):
        return


    def print(self):
        return self.values





example = Store()
list = [1,2,3,4,5,6]

for a in list:
    example.insert(a)

print(example.print())
print(example.remove(2))
print(example.get_random())


