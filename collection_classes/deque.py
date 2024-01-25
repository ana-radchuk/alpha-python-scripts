import collections
import string

# initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# deques support the len() func
print(f"Item count: {len(d)}")

# deques can be iterated over
for e in d: 
    print(e.upper())

# manipulate items from either end
d.pop()
d.popleft()
d.append(2)
d.appendleft(1)
print(d)

# use an index to get a particular item
print(d)
d.rotate(1)
print(d)

