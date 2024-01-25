from collections import Counter

class1 = ["Bob", "James", "Chad", "Hannah", "Penny", "Darcy", "James"]
class2 = ["Bill", "Barry", "Cindy", "Sam", "James", "Gabby"]

# counter for class1 and class2
c1 = Counter(class1)
c2 = Counter(class2)

# how many students named James
print(c1["James"])

# how many students in class 1
print(sum(c1.values()), "students in class 1")

# combine the two classes
c1.update(class2)
print(sum(c1.values()), "students in class 1")

# the most common name in the two classes
print(c1.most_common(2))

# separate two classes again
c1.subtract(class2)
print(c1.most_common(1))

#  most common between the two classes
print(c1 & c2)

