# 1) vars: 3

# 2) input: 1, 4, 5

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

# 4) matrix:
#
#     AB 
#   \ _00___01___11___10_
# C 0|_0__|_0__|_0__|_1__|
#   1|_1__|_0__|_0__|_1__|

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

    i = 0
    while i < var_count:
        i += 1
        bit = 0

        if val % 2 != 0:
            bit = 1
            bits.append(bit) 

        if (val <= 1):
            break

        val /= 2

    missing_bits = var_count - len(bits)
    while missing_bits > 0:
        missing_bits -= 1
        bits.append(0)

    return bits

def get_result(number):
    global ones

    for one in ones:
        if one == number:
            return 1

    return 0

def print_truth_table():
    global ones
    global var_count

    print_table_header()
    print_table_rows()
    
def print_table_header():
    global var_count
    global variables

    header = '|n|'
    for i in range(0, var_count):
        header += variables[i] + '|'
    header += 'r|'

    print(header)
    
def print_table_rows():
    global var_count
    global ones

    size = pow(2, var_count)

    for i in range(0, size):
        row = '|' + str(i) + '|'
        result = get_result(i)
        bits = get_binary_value(i)

        for bit in bits:
            row += str(bit) + '|'
    
        row += str(result) + '|'
        print(row)


setup()
print_truth_table()