"""These are examples of manipulating Strings"""


first_name = "Soleman"
last_name = "Zaghlool"

#Print Letters
print (first_name[0])
print (first_name[1])
print (first_name[2])
print (first_name[3])
print (first_name[4])
print ("\n")

#Print letters using for loop
for letter in last_name:
    print(letter)

#Multiline string
multi = """Test1
Test2
Test3"""
print (multi)

#int/str conversion
x = "5"
y = 3

sum = int(x) + y
print(sum)

#Joining strings
conc = x + str(y)
print(conc)

#format print
print(f"joining x, and y results in {conc}")

#Convert multiple lines into a list of lines, then list of words

long_text = """line1a line1b line1c line1d
line2a line2b line2c line2d
line3a line3b line3c line3d
line4a line4b line4c line4d
line5a line5b line5c line5d
line6a line6b line6c line6d"""
print (long_text)

long_text_list = long_text.splitlines()
print (long_text_list)

word_list = []

for line in long_text_list:
    word_list = line.split()
    print (word_list)
