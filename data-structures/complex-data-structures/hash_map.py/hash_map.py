class Hash_Map:
    def __init__(self, size = 10):
        self.data = {}
        self.max_size = size
    
    def get(self, key: str):
        hash_code = self.hash(key)
        values = self.data[hash_code]

        for current_key,value in values:
            if current_key == key:
                return value

    def put(self, key: str, value):
        hash_code = self.hash(key)
        if not self.data.keys().__contains__(hash_code):
            self.data[hash_code] = [(key, value)]
        else:
            self.data[hash_code].append((key, value))


    def hash(self, key: str):
        hash_code = 0
        for character in key:
            hash_code += ord(character)
        return hash_code % self.max_size
    
    def __str__(self):
        return str(self.data)

test_map = Hash_Map(5)
test_map.put("Owens", "Ehimen")
test_map.put("Johnny", "Bravo")
test_map.put("Comfort", "Survival")
print(test_map)

print(test_map.get("Owens"))
