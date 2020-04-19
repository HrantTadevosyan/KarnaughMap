# 1) vars: 3
#     
#----------------code--------------------   
#    count = 3 

# 2) input: 1, 4, 5
# 
#----------------code--------------------  
#    ones = [1, 4, 5]

# 3) table:
# 
#   A | B | C | r
#  ---------------
#   0 | 0 | 0 | 0 -> 0
#   0 | 0 | 1 | 1 -> 1
#   0 | 1 | 0 | 0 -> 2
#   0 | 1 | 1 | 0 -> 3
#   1 | 0 | 0 | 1 -> 4
#   1 | 0 | 1 | 1 -> 5
#   1 | 1 | 0 | 0 -> 6
#   1 | 1 | 1 | 0 -> 7
#
#----------------code--------------------  
#    size = 2 ^ count = 8

# 4) matrix:
#
#     AB 
#   \ _00___01___11___10_
# C 0|_0__|_0__|_0__|_1__|
#   1|_1__|_0__|_0__|_1__|
#  
#----------------code--------------------  
#  cols = size / 2 = 4
#  rows = size / cols = 2
#  
#  def get_value(number):
#      for one in ones:
#          if number == one:
#              return 1
#
#      return 0
#  
#  def to_binary(number):
#      arr = []
#
#  def fill():
#      for number in range(0, size - 1):  
#          val = get_value(number)
#          col = number 

# 5) output:
#
#   F = CA'B' + AB'
#
var_count = -1
ones = list()
variables = ['A', 'B', 'C', 'D', 'E', 'F']

def setup():
    global var_count
 
    min_var_count = 2
    max_var_count = 6

    print('enter the var count: ')
    var_count = int(input())

    if var_count > max_var_count:
        var_count = max_var_count
    if var_count < min_var_count:
        var_count = min_var_count

    setup_ones(var_count)

def setup_ones(count):
    global ones

    one = -1
    while len(ones) < count:
        print('fill up the ones: ' )
        one = int(input())
        ones.append(one)

def get_binary_value(number):
    global var_count

    bits = list()
    val = number

    for i in range(0, var_count):
        bit = 0
        if val % 2 != 0:
            bit = 1
            bits.append(bit) 
        val /= 2

    return bits


def print_truth_table():
    global ones
    global var_count

    print_table_header()
    
def print_table_header():
    global variables

    header = '|'
    for i in range(0, len(variables)):
        header += variables[i] + '|'
    header += 'r|'

    print(header)
    
def print_table_rows():
    global var_count
    global ones

    size = pow(2, var_count)


setup()
print_truth_table()