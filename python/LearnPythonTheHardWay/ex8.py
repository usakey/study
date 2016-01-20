tabby_cat = "\tI'm \"tabbled\" in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* cat food
\t* fishies
\t* catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

'''
fun code to play with
'''
while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,
