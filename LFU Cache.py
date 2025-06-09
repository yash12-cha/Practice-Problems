class Node:
    def __init__(self, key, val):
        self.key = key  # Key of the cache entry
        self.val = val  # Value of the cache entry
        self.prev = None  # Pointer to the previous node in the DLL
        self.next = None  # Pointer to the next node in the DLL
        self.freq = 1  # Frequency counter starts at 1


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail  # Head next points to tail
        self.tail.prev = self.head  # Tail prev points to head
        self.size = 0  # Tracks number of actual nodes (not dummy)

    def _insert(self, node):
        # Insert a node right after the head (most recently used position)
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def _remove(self, node):
        # Remove a node from its position in the DLL
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity  # Maximum number of items allowed
        self.cache = {}  # Maps key to its Node
        self.freqlistmap = {}  # Maps freq to its corresponding DLL
        self.minfreq = 0  # Minimum frequency of any node in the cache

    def update_freqlistmap(self, node):
        # Remove node from current frequency list
        current_freq = node.freq
        self.freqlistmap[current_freq]._remove(node)

        # If current list becomes empty and was the minimum frequency, update minfreq
        if (
            current_freq == self.minfreq
            and self.freqlistmap[current_freq].size == 0
        ):
            self.minfreq += 1

        # Increment node's frequency
        node.freq += 1
        new_freq = node.freq

        # Add node to the new frequency list
        if new_freq not in self.freqlistmap:
            self.freqlistmap[new_freq] = DoublyLinkedList()
        self.freqlistmap[new_freq]._insert(node)

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1  # Key not found

        self.update_freqlistmap(node)  # Update its frequency
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return  # No capacity to store items

        if key in self.cache:
            # Key exists, update value and frequency
            node = self.cache[key]
            node.val = value
            self.update_freqlistmap(node)
        else:
            # Key doesn't exist and cache is full -> evict LFU node
            if len(self.cache) == self.capacity:
                lst = self.freqlistmap[self.minfreq]
                evict_node = (
                    lst.tail.prev
                )  # Least recently used in the minfreq list
                lst._remove(evict_node)
                del self.cache[evict_node.key]

            # Reset minfreq to 1 for new node
            self.minfreq = 1

            # Insert new node
            if self.minfreq not in self.freqlistmap:
                self.freqlistmap[self.minfreq] = DoublyLinkedList()

            node = Node(key, value)
            self.freqlistmap[self.minfreq]._insert(node)
            self.cache[key] = node

if __name__ == "__main__":
    # Example operations
    lfu = LFUCache(2)
    print(lfu.put(1, 1))     # cache = {1=1}
    print(lfu.put(2, 2))     # cache = {1=1, 2=2}
    print(lfu.get(1))        # return 1, freq of 1 becomes 2
    print(lfu.put(3, 3))     # evicts key 2 as it has lower freq, cache = {1=1, 3=3}
    print(lfu.get(2))        # return -1 (not found)
    print(lfu.get(3))        # return 3
    print(lfu.put(4, 4))     # evicts key 1, cache = {3=3, 4=4}
    print(lfu.get(1))        # return -1 (not found)
    print(lfu.get(3))        # return 3
    print(lfu.get(4))        # return 4


'''
⏱️ Time Complexity:

get(key) – O(1) on average
Hash map lookup is O(1) average-case.
Removing and inserting the node in the doubly linked list takes O(1).
put(key, value) – O(1) on average
Checking or inserting into the hash map is O(1).
Removing an old node or inserting a new one in the linked list is O(1).

📦 Space Complexity:

O(N), where N = capacity
You store up to capacity key-node pairs in the hash map.
You also maintain up to capacity nodes in the doubly linked list.
Overall, the space usage grows linearly with capacity.
'''