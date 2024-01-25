from collections import defaultdict

fruits = ['apple', 'pear', 'orange', 'banana', 
          'apple', 'grape', 'banana', 'banana']

fruitCounter = defaultdict(lambda: 100) # or just int

# count the elements in the list
for f in fruits: 
    fruitCounter[f] += 1

print(fruitCounter)


