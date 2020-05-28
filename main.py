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
matrix = list()
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
    while True:
        print('fill up the ones(press [q] to QUIT): ')
        inp = input() 
        if (inp == 'q'):
            break

        one = int(inp)
        ones.append(one)

def get_binary_value(number):
    global var_count

    bits = list()
    val = number

    i = 0
    while i < var_count:
        i += 1
        bit = 0

        val = int(val)
        if val % 2 != 0:
            bit = 1
        
        bits.append(bit) 

        if (val < 1):
            break

        val /= 2

    missing_bits = var_count - len(bits)
    while missing_bits > 0:
        missing_bits -= 1
        bits.append(0)

    bits.reverse()
    return bits

def get_result(number):
    global ones

    for one in ones:
        if one == number:
            return 1

    return 0

def solve():
    global ones
    global var_count

    cl = []
    fl = []
    
    s = len(ones)
    for i in range(0, s - 1):
        for j in range(i + 1, s):
            n1 = ones[i]
            n2 = ones[j]

            bits1 = get_binary_value(n1)
            bits2 = get_binary_value(n2)

            collision = 0
            for k in range(0, var_count):
                if bits1[k] != bits2[k]:
                    collision += 1

            if (collision <= 1):
                if (n1 not in cl) and (n2 not in cl):
                    cl.append(n1)                    
                    cl.append(n2)

                    bits = get_bits_diff(bits1, bits2)
                    fl.append(bits)

    xorl = [item for item in ones if item not in cl]

    for xor in xorl:
        bits = get_binary_value(xor) 
        fl.append(bits)

    return fl

def get_bits_diff(bits1, bits2):
    global var_count

    bits = list()

    for i in range(0, var_count):
        if bits1[i] != bits2[i]:
            bits.append(-1)
        else:
            bits.append(bits1[i])

    return bits

def make_function(sl):
    global variables

    output = 'F = '

    for s in sl:
        for i in range(0, len(s)):
            if (s[i] == 1):
                output += variables[i] 
            elif (s[i] == 0):
                output += variables[i] + '\''
        
        output += '+'

    output = output[:-1]
    return output

def print_all():
    print_truth_table()

def print_truth_table():
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
print_all()

sl = solve()
print(sl)
o = make_function(sl)
print(o)