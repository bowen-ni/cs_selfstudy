from LInked_list import Node,LinkedList
from blossom_lib import flower_definitions

class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for _ in range(self.array_size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        payload = Node([key,value])
        exist = False
        list_at_array = self.array[array_index]
        for item in list_at_array:
            if item[0] == key:
                item[1] = value
                exist = True
        if exist == False:
            list_at_array.insert(payload)


    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        list_at_array = self.array[array_index]
        for item in list_at_array:
            if item[0] == key:
                return(item[1])
        return(None)


blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
    blossom.assign(flower[0],flower[1])

choice = input("Enter the flower name")
print(blossom.retrieve(choice))
