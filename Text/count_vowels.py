# Count Vowels
# Enter a string and the program counts the number of vowels in the text.
# For added complexity have it report a sum of each vowel found.

vowels = list('aeiou')
vowel_sum = 0

s = input('Enter a string: ')

for vowel in vowels:
    print(f'\'{vowel.upper()}\' count in word: {s.count(vowel)}')
    vowel_sum += s.count(vowel)

print(f'Vowels sum: {vowel_sum}')
