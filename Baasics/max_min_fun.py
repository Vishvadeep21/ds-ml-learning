# syntax== max(iterable,key= ,default=)
# syntax== min(iterable,key= ,default=)
a=1,2,3,4,5
print(max(a))
print(min(a))

# in key we can give on what baises we want to sort max or min 
# in default we can give what will be the default o/p

word_count = {"apple": 5, "banana": 3, "grape": 6}

# Find the key with the maximum and minimum value (count)
max_word = max(word_count, key=word_count.get)  # 'grape'
min_word = min(word_count, key=word_count.get)  # 'banana'

print(f"Word with max count: {max_word}, Word with min count: {min_word}")