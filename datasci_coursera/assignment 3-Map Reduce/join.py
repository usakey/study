import MapReduce
import sys

"""
Relational Join Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: the entire record, i.e the line
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)
    
def reducer(key, list_of_values):
    # key: order_id
    # value: list of appended records
    orderList = []
    itemList = []
    for sub_record in list_of_values:
        if sub_record[0] == 'order':
            orderList.append(sub_record)
        elif sub_record[0] == 'line_item':
            itemList.append(sub_record)
    
    ## list comprehension for cross product
    cross_product = [[x, y] for x in orderList for y in itemList]
    for i in range(len(cross_product)):
        order_res= cross_product[i][0]
        item_res = cross_product[i][1]

        mr.emit(order_res + item_res)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
