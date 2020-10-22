from string import ascii_lowercase

text = """Alice was beginning to get very tired of sitting by her sister
            on the bank, and of having nothing to do: once or twice she had peeped
            into the book her sister was reading, but it had no pictures
            or conversations in it, 'and what is the use
            of a book,' thought Alice 'without pictures or conversation?'"""

letter_count = {}

for l in ascii_lowercase:  # abcd...z
    letter_count[l] = 0

for let in text:
    let = let.lower()
    if let in letter_count:
        letter_count[let] += 1

for let, count in letter_count.items():
    print(f'{let} is used {count:3d} times')

print('\n\n\n')

word_count = {}

for word in text.split():
    word = word.lower()
    word_count.setdefault(word, 0)
    word_count[word] += 1

for w, count in word_count.items():
    print(f'{w:14} is used {count:3d} times')

print('\n\n\n')


# The 5 most used words
# need to sort by the value in the (key,value) tuple

# option 1
def get_second(tpl):
    """Return the second element"""
    return tpl[1]


sorted_result = sorted(word_count.items(), key=get_second, reverse=True)

# option 2, python has "get_second" built-in as "itemgetter"
# from operator import itemgetter
# sorted_result = sorted(word_count.items(), key=itemgetter(1), reverse=True)

print('The 5 most common words')
for w, c in sorted_result[:5]:
    print(f'{w:14} is used {c:3d} times')