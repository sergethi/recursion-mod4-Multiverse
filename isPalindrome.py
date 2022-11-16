
# // A palindrome is a word that is spelled the same forwards and backwards.
# // For example, "LEVEL", "RACECAR", and "KAYAK" are all palindromes, while "MOTOR", "RUDDER", and "DOGGED" are not palidromes.
# // Write a recursive function, isPalindrome, to check if a string is a palindrome.
# // Return true if the string is a palindrome; otherwise, return false.

def isPalindrome(word):
    word = word.lower()
    outPut = ""

    def recursion(input):
        nonlocal outPut
        if len(input) == 1:
            return input
        last = input[-1]
        outPut += last + recursion(input[:-1])
        return outPut
    recursion(word)
    return outPut == word


print(isPalindrome('Kayak')) # => true
# isPalindrome('NEVERODDOREVEN'); // => true
# isPalindrome('Tacocat'); // => true
# isPalindrome('SELFLESS'); // => false