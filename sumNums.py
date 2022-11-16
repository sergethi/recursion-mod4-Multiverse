
# Write a function, sumNums, that takes a number, num, as an argument and returns the sum of all the numbers between 1 and num.
# You can assume that num will be greater than 1. Use recursion.


def sumNums(num):
    if num == 1:
        return 1
    return num + sumNums(num-1)

print(sumNums(3)); # => 6 (3 + 2 + 1)