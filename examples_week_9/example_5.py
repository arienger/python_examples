# 3 ways of getting information from a file

with open('timemachine.txt', encoding="utf8") as f:
    for line in f:
        l = len(line)
        print('The line is', l, 'long, and starts with')
        print('>>>', line[0:20], '<<<')

# ========

with open('timemachine.txt', encoding="utf8") as f:
    all_lines = f.readlines()

print(len(all_lines), 'lines in the text')

# ==========

with open('timemachine.txt', encoding="utf8") as f:
    all_lines = f.read()

print("vvvvvvv")
print(all_lines)
print("^^^^^^^")

# ========

with open('numbers.txt', 'w', encoding="utf8") as f:
    for i in range(100):
        f.write(f'{i} is a nice number\n')

# now open the file numbers.txt in your editor and see what's inside

# write other files!