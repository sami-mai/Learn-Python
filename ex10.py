# Exercise 10: What Was That?
# Escape Sequences
tabby_cat = "\tI'm tabbed in." # \t is horizontal tab
persian_cat = "I'm split\non a line." # \n is new line
backslash_cat = "I'm \\ a \\ cat." # \\ is backlash

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# while loop
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i, # \r is Carriage return
