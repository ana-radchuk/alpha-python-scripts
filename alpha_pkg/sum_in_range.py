# easy sum first 100 numbers
def range_sum(n):
    sum = 0
    for i in range (1, n + 1):
        sum = sum + i
    return sum

# recursively sum first 100 numbers
def recursive_sum(n):
   if n <= 1:
       return n
   else:
       return n + recursive_sum(n - 1)
   
# arithmetically sum first 100 numbers
# arithmetic progression: S = n/2 [2a + (n – 1) * d]
def math_sum(n):
    return int((n/2) * (2 + (n - 1) * 1))

# print(f'sum_in_range.py module name is {__name__}')
# if __name__ == '__main__':
#    print('This is a module. Please import using: \nimport sum_range.py')
