print("\nPERFECT NUMBER DETERMINATOR FOR ALF\n")
number = int(input("Please, enter a non-negative number: "))
orig_num = number

sum_divisors = 0
perfect = 1

if number < 0:
    print("Negative numbers can't be a perfect number.")
else:
    while perfect < number:
        if number % perfect == 0:
            sum_divisors += perfect
        perfect += 1

    if number == sum_divisors:
        print("%d is a Perfect Number." % (orig_num))
    else:
        print("%d is NOT a Perfect Number." % (orig_num))