# 1. Definition of dictionaries, common scenarios when they are useful, main supported operation, time and space complexity. 

# Definition is a storage of information where you type a key that is connected to the element of a dictionary and by entering the key you receive the content that the key is linked to.
# The key can be a string, integer and other type of information. But it cannot be a list.
# The dictionary is more usefull in the kind of scenarios that need a somekind of keyword and you get the content, defenition of the word by entering it.
# For example your keyword is "name" and you get "alexandr" by entering it. So in conclusion the dictionary in python can be used for making a literal dictionary or giving words or 
# different types of information their meaning and content.
# 1. def add(key: str, value: str)
# 2. def delete(key: str)
# 3. read 
# 4. replace the value of the key with a new one

#words = {"fruit": "apple", "flower": "orchid"}
#words["fruit"] = "banana"
#print(words["fruit"])


# 100_000_000 million kv pairs in dictionary A
# 100_000_000 million values in array B 

# How much time approximately it will take to read 100e6 values from dictionary A vs array B 
# O(1) for 1 lookup (time complexity)

# A hash function is a function that turns a 


def character_hash(name: str):
    """Simplistic hash function for character names."""
    return sum(ord(c) for c in name[:3]) % 100

# Example character names 
# https://en.wikipedia.org/wiki/Unicode 
characters = ["Zelda", "Link", "Ganon", "Mario", "Luigi", "Bowser", "Peach"]

# Create a dictionary to map hash values to character names
hash_table = {}

for character in characters: 
    hash_key = character_hash(character)
    if hash_key in hash_table:
        print(hash_table[hash_key], character)
    else:
        hash_table[hash_key] = character

