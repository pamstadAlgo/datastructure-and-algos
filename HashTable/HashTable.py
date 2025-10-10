

class HashTable:
    """
    Implements a hash table with the modulos function as the hash function
    """
    def __init__(self, size=20):
        self.hash_table = [None]*size
        self.size = size

    def modulos_hash_function(self, item):
        return item % self.size
    
    def linear_probing(self, start_index, item):
        """
        Returns a free index found by linear probing
        """
        for i in range(start_index + 1, self.size):
            if self.hash_table[i] is None or self.hash_table[i] == item:
                return i
            
        #if no free space anymore return None
        return None
    
    def __str__(self):
        return str(self.hash_table)

    def put(self, item):
        """
        Places the item in the hash function. In case of a hash collision we apply linear probing
        """
        #apply the hash function to the input value
        hash_index = self.modulos_hash_function(item)

        #check for hash collision
        if self.hash_table[hash_index] is None or self.hash_table[hash_index] == item:
            self.hash_table[hash_index] = item
        elif self.hash_table[hash_index] != item:
            #do linear probing
            hash_index = self.linear_probing(start_index=hash_index, item=item)

            print('this is hash index of linear probing: ', hash_index)

            #check if index was found with linear probing
            if hash_index is not None:
                self.hash_table[hash_index] = item
            else:
                print(f"No more space in the hash table, we were not able to find a place for item {item}")

    def get(self, item):
        """
        Returns true if the item is in the hash table, false otherwise
        """
        pass



ht = HashTable()

ht.put(20)
ht.put(22)
ht.put(53)
ht.put(1)
ht.put(21)

print(ht)
