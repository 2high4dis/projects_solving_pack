# Count Words in a String
# Counts the number of individual words in a string.
# For added complexity read these strings in from a text file and generate a summary.

file = open(r'count_words.txt')

words_count = 0

for line in file.readlines():
    words_count += len(line.split())

print(words_count)
