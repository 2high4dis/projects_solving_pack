# Pig Latin
# Pig Latin is a game of alterations played on the English language game.
# To create the Pig Latin form of an English word the initial consonant sound is
# transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay).
# Read Wikipedia for more information on rules.

s = input('Enter an English word: ')

pig_s = s[1:] + s[:1] + 'ay'
print(f'Pig latin word for \'{s}\': {pig_s}')
