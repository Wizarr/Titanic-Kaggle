tabby_cat = "\tI', tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll make a list
\t* cattots
\t* wine
\t* beer\n\t* smokes
"""


print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
