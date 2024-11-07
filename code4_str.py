"""These are examples of manipulating Strings"""

FIRST_NAME = "Soleman"
LAST_NAME = "Zaghlool"

# Print Letters
print(FIRST_NAME[0])
print(FIRST_NAME[1])
print(FIRST_NAME[2])
print(FIRST_NAME[3])
print(FIRST_NAME[4])
print("\n")

# Print letters using for loop
for letter in LAST_NAME:
    print(letter)

# Multiline string
MULTI = """Test1
Test2
Test3"""
print(MULTI)

# int/str conversion
X = "5"
Y = 3

TOTAL = int(X) + Y
print(TOTAL)

# Joining strings
CONC = X + str(Y)
print(CONC)

# format print
print(f"joining x, and y results in {CONC}")

# Convert multiple lines into a list of lines, then list of words

LONG_TEXT = """line1a line1b line1c line1d
line2a line2b line2c line2d
line3a line3b line3c line3d
line4a line4b line4c line4d
line5a line5b line5c line5d
line6a line6b line6c line6d"""
print(LONG_TEXT)

LONG_TEXT_list = LONG_TEXT.splitlines()
print(LONG_TEXT_list)

word_list = []

for line in LONG_TEXT_list:
    word_list = line.split()
    print(word_list)
