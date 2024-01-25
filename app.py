from alpha_pkg.sum_in_range import * 

while True:
    try:
        x = int(input("Please enter integer >= 0 and < 100: "))

        if x <= 0 or x > 100:
            raise ValueError
        
        range = range_sum(x)
        recursive = recursive_sum(x)
        math = math_sum(x)

        print("Range method => " + str(range))
        print("Recursive method => " + str(recursive))
        print("Arithmetic method => " + str(math))

        if range == recursive == math:
            print("Calculated correctly")
        else:
            print("Invalid calculation")

        break

    except ValueError:
        print("That was not a valid number. Try again")

    

