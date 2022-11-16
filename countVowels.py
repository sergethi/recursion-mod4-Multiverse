# Write a function, countVowels, that accepts a string as an argument and returns the number of vowels in that string.
# Use recursion.
def countVowels(phrase):
    vowels = 'aeiou'
    if len(phrase) == 0:
        return 0
    if phrase[-1] in vowels:
        return 1 + countVowels(phrase[:-1])
    
    return 0 + countVowels(phrase[:-1])






print(countVowels('Four')); # => 2
print(countVowels('Four score and seven years')); # => 9