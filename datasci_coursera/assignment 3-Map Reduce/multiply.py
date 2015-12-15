import MapReduce
import sys

"""
matrix multiply Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    m = record[0]
    i = record[1]
    j = record[2]
    v = record[3]
        
    if m == 'a':
        for k in range(5):
            key = (i, k)
            mr.emit_intermediate(key, (m, j, v))
    elif m == 'b':
        for l in range(5):
            key = (l, j)
            mr.emit_intermediate(key, (m, i, v))
    else:
        print 'invalid input'
    
def reducer(key, list_of_values):
    row = key[0]
    col = key[1]
    ma = []
    mb = []
    cnt_a = 0
    cnt_b = 0
    for value in list_of_values:
        if value[0] == 'a':
            while value[1] != cnt_a:
                ma.append(0)
                cnt_a += 1
            ma.append(value[2])
            cnt_a += 1
        else:
            while value[1] != cnt_b:
                mb.append(0)
                cnt_b += 1
            mb.append(value[2])       
            cnt_b += 1
    if cnt_a == 4:
        ma.append(0)
    if cnt_b == 4:
        mb.append(0)
    res = sum(m * n for m, n in zip(ma, mb))  
    mr.emit((row, col, res))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
