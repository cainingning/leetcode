class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.hash_map.get(val, None) == None:
            self.hash_map[val] = val
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.hash_map.get(val, None) == None:
            return False
        self.hash_map.pop(val)

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if len(self.hash_map) == 0:
            return 0
        import random
        x = random.randint(0, len(self.hash_map) - 1)
        count = 0
        for k, v in self.hash_map.items():
            if count == x:
                return k
            count += 1

        return 0

if __name__ == '__main__':
    solution = RandomizedSet()
    print(solution.insert(), solution.hash_map)
    print(solution.remove(2), solution.hash_map)
    print(solution.insert(2), solution.hash_map)
    print(solution.getRandom())