class RandomizedSet:

    def __init__(self):
        self.items_array = []
        self.index_map = {} # item: index
        
    # if item not in the index_map, map item: index, append to items_array
    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        index = len(self.index_map)
        self.index_map[val] = index
        self.items_array.append(val)
        return True
    
    # if item in the index_map, remove it, get its index, edit that index in items_array
    # to the last element, change that element's value in index_map
    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        index = self.index_map.pop(val)
        last_item = self.items_array.pop()
        if last_item != val:
            self.index_map[last_item] = index
            self.items_array[index] = last_item
        return True
    
    # get a random element from the array
    def getRandom(self) -> int:
        return random.choice(self.items_array)        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()