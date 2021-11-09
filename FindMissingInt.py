#!/usr/bin/python3
import random

# A sneaky number is missing from this list? Which one is it?
# Given a randomly ordered list of unique integer numbers where the list has all the numbers from 1-N,
# except that is missing one number in the sequence. How would you approach finding out the missing number?

N = 100
numbers_original = [x for x in range(0, N+1)]
random.shuffle(numbers_original)

# One of our numbers ran away!
numbers_missing_element = numbers_original.copy()
missing_element = numbers_missing_element.pop(random.randint(0, len(numbers_missing_element) - 1))
print("Shhhh! The sneaky number is {0}".format(missing_element))

# --------------------------------------------------------------------------------------------------------------------

# First approach - dumb N * N
for n in numbers_original:
    if n not in numbers_original:
        print("N*N Compare: The sneaky number must be {0}".format(n))
        break

# --------------------------------------------------------------------------------------------------------------------

# Second approach- addition difference
total_of_n_numbers = sum(numbers_original)
total_with_missing_number = sum(numbers_missing_element)
difference = total_of_n_numbers - total_with_missing_number
print("Difference Method: The sneaky number must be {0}".format(difference))

# --------------------------------------------------------------------------------------------------------------------

# Third approach, cheeky python set difference... this would be my default in python which I've done before lol
s1 = set(numbers_original)
s2 = set(numbers_missing_element)
diff = [x for x in s1 - s2]
print("Set difference method: The sneaky number must be {0}".format(diff[0]))

# --------------------------------------------------------------------------------------------------------------------

# Sharad Gupta hinted that there was a another method using factorization. Still trying to work that one out!

# --------------------------------------------------------------------------------------------------------------------

# A friend told me to look up Gauss' trick- this is a better way of summation for the original elements and results
# in a single rather than two iterations for summation - this also let me find a bug in my code where I was planning on
# N elements but actually assigning N-1 elements which broke the N + 1 part of this formula.
total = (N * (N + 1)) / 2
print("Difference Method with Gauss' Trick: The sneaky number must be {0}".format(total - total_with_missing_number))
