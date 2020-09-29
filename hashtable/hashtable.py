class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_head(self, node):
		node.next = self.head
		self.head = node

	def find_key(self, key):
		cur = self.head

		while cur is not None:
			if cur.key == key:
				return cur

			cur = cur.next

		# If we get here, it's not in the list
		return None
		
	def delete(self, key):

		# Special case of empty list​
		if self.head is None:
			return None

		# Special case of deleting the head of the list​
		if self.head.key == key:
			old_head = self.head
			self.head = self.head.next
			old_head.next = None
			return old_head

		# General case​
		prev = self.head
		cur = self.head.next

		while cur is not None:
			if cur.key == key:
				prev.next = cur.next
				cur.next = None
				return cur

			prev = prev.next
			cur = cur.next
		# If we get here, we didn't find it
		return None
			

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [LinkedList()] * self.capacity
        self.items = 0
        


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        load_factor = self.items / self.capacity
        return load_factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hash_ = 14695981039346656037
        bytes_list = str(key).encode()
        for b in bytes_list:
            hash_ = hash_ * 1099511628211
            hash_ = hash_ ^ b
        return hash_

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        bytes_list = str(key).encode()
        total = 0
        for b in bytes_list:
            total += b
        return total


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        ll = self.data[self.hash_index(key)]
        if ll.head == None:
            ll.head = HashTableEntry(key, value)
            self.items += 1
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity*2)
        elif ll.find_key(key) == None:
            ll.insert_at_head(HashTableEntry(key, value))
            self.items += 1
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity*2)
        else:
            old_entry = ll.find_key(key)
            old_entry.value = value


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        ll = self.data[self.hash_index(key)]
        var = ll.delete(key)
        if var == None:
            print("Warning, can't delete because it doesn't exist.")
            return None        
        else:
            self.items -= 1
            return var

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        ll = self.data[self.hash_index(key)]
        if ll.find_key(key) == None:
            return None
        else:
            return ll.find_key(key).value


    def resize(self, new_capacity):
    #def resize(self):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        #if self.get_load_factor() > 0.7:
        old_data = self.data
        self.items = 0
        self.capacity = new_capacity
        self.data = [LinkedList()] * self.capacity
        for i in old_data:
            cur = i.head
            while cur != None:
                self.put(cur.key, cur.value)
                cur = cur.next


# ht = HashTable(8)
# print(ht.data)
# ht.put("line_1", "'Twas brillig, and the slithy toves")
# print(ht.get("line_1").value)
# print(ht.items)
# ht.delete("line_1")
# print(ht.get("line_1").value)
# print(ht.items)

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
