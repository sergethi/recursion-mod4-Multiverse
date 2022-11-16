# Write a function, sumDigits, that sums up all the digits of a number passed in as an argument.
# You can assume that the argument will be a positive integer. Use recursion.


def sumDigits(digits):
    numToString = str(digits)
    total = 0
    def recursion(strings):
        print(strings)
        nonlocal total
        if len(strings) == 1:
            return strings
        lastDigit = strings[-1] # 4
        
        total += int(lastDigit) + int(recursion(strings[:-1]))

    recursion(numToString)
    return total


print(sumDigits(1234)) # => 10

# def sumDigits(123):
#     numToString = str(digits)
#     if len(numToString) == 1:
#         return int(numToString)
#     lastDigit = digits[:-1] # 3
#     return 3 +3

# def sumDigits(12):
#     numToString = str(digits)
#     if len(numToString) == 1:
#         return int(numToString)
#     lastDigit = digits[:-1] # 2
#     return 2 + 1

# def sumDigits(1):
#     numToString = str(digits)
#     if len(numToString) == 1:
#         return int(numToString)
#     lastDigit = digits[:-1] # 3
#     return int(lastDigit) + sumDigits(digits)