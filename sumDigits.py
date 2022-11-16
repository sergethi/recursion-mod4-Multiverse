# Write a function, sumDigits, that sums up all the digits of a number passed in as an argument.
# You can assume that the argument will be a positive integer. Use recursion.


def sumDigits(digits):
    numToString = str(digits)
    total = 0
    def recursion(strings):
        nonlocal total
        if len(strings) == 1:
            return strings
        lastDigit = strings[-1] # 4
        
        total += int(lastDigit) + int(recursion(strings[:-1]))
        return total
    recursion(numToString)
    return total


print(sumDigits(1234)) # => 10

