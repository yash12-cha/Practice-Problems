class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail to simplify inserts/removals
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove an existing node from the list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, node):
        """Insert node just after head (mark as MRU)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """Return the value of key if present; else -1. Mark as recently used."""
        node = self.cache.get(key)
        if not node:
            return -1
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key with value.
        If capacity exceeded, evict least-recently-used (LRU) item.
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert(node)
        else:
            if len(self.cache) == self.capacity:
                # Evict LRU
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._insert(new_node)


# Driver code to test the sequence of operations
if __name__ == "__main__":
    # Define operations and their arguments
    operations = [
        "LRUCache",
        "put",
        "put",
        "get",
        "put",
        "get",
        "put",
        "get",
        "get",
        "get",
    ]
    arguments = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    # This will hold results: None for constructors/put, and actual returns for get
    results = []

    cache = None
    for op, arg in zip(operations, arguments):
        if op == "LRUCache":
            cache = LRUCache(arg[0])
            results.append(None)
            print(f"Initialized LRUCache with capacity = {arg[0]}")
        elif op == "put":
            cache.put(arg[0], arg[1])
            results.append(None)
            print(f"put({arg[0]}, {arg[1]})")
        elif op == "get":
            val = cache.get(arg[0])
            results.append(val)
            print(f"get({arg[0]}) -> {val}")

    print("\nFinal results:", results)
    # Expected: [None, None, None, 1, None, -1, None, -1, 3, 4]

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