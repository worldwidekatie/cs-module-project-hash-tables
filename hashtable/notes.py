

HASH_DATA_SIZE = 8
hash_data = [None] * HASH_DATA_SIZE

def hash_function(s):
    """Naive hashing function don't use in production"""
    # This is bad because it has collisions
    # e.g. Goats and oGats are the same number
    bytes_list = str(s).encode()
    total = 0
    for b in bytes_list:
        total += b
    return total

def get_index(s):
    hash_value = hash_function(s)

    return hash_value % HASH_DATA_SIZE

def put(k, v):
    """For a given key, store a value in the hash table"""
    # will overwrite which is good/norml for a dictionary
    index = get_index(k)
    hash_data[index] = v

def get(k):
    index = get_index(k)
    return hash_data[index]


print(hash_data)
put("Beej!", "Hello, world!")
print(get("Beej!")) # should print hello world
print(hash_data)
print(get("Goats"))



