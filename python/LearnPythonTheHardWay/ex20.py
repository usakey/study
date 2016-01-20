from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "let's print the whole file \n"
print_all(current_file)

print "let's rewind \n"
rewind(current_file)

print "print fist line \n"
print_a_line(1, current_file)