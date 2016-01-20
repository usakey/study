def readfile(filename):
	lines = [line for line in file(filename)]

	# first line is the column titles
	colnames = lines[0].strip().split('\t')[1:]
	rownames = []

	data = []
	for line in lines[1:]:
		p = line.strip().split('\t')
		# first column in each row is the rowname
		rownames.append(p[0])

		# the remainder of the row as the data
		data.append([float(x) for x in p[1:]])
	return rownames, colnames, data

# rownames, colnames, data = readfile('blogdata.txt')
# print data

 