class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.useCounter = defaultdict(int)
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
    
    def insert(self, node):
        prev, next = self.right.prev, self.right
        node.prev, node.next = prev, next
        prev.next, next.prev = node, node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.useCounter[key] += 1
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key].value = value
            self.insert(self.cache[key])
            self.useCounter[key] += 1
        else:
            if len(self.cache) == self.capacity:
                minValue = min(self.useCounter.values())
                minValueCount = Counter(self.useCounter.values())
                if minValueCount[minValue] > 1:
                    lruKeys = set()
                    for k in self.useCounter:
                        if self.useCounter[k] == minValue:
                            lruKeys.add(k)
                    
                    curr = self.left.next
                    while curr != self.right and curr.key not in lruKeys:
                        curr = curr.next
                    self.remove(curr)
                    del self.cache[curr.key]
                    del self.useCounter[curr.key]
                else:
                    lruKey = None
                    for k in self.useCounter:
                        if self.useCounter[k] == minValue:
                            lruKey = k
                            break
                    self.remove(self.cache[lruKey])
                    del self.cache[lruKey]
                    del self.useCounter[lruKey]
            node = Node(key, value)
            self.cache[key] = node
            self.useCounter[key] += 1
            self.insert(node)






        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)