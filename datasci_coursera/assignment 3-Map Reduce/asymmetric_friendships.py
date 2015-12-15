import MapReduce
import sys

"""
Asymmetric Friend Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person name
    # value: friend name
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: person name
    # value: list of appended friends
    for friend in list_of_values:
        try:
            reverse_list = mr.intermediate[friend]
            if key not in reverse_list:
                mr.emit((key, friend))
                mr.emit((friend, key))
        except KeyError:
            mr.emit((key, friend))
            mr.emit((friend, key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
