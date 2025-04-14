def ones_in_32_bit(num):
    count = 0
    sqrt_floor = int(num**(1/2))

    for i in range(sqrt_floor, -1, -1):
        if 2**i <= num:
            count += 1
            num = num - 2**i
        i -= 1
    
    return count

#num = int('11110000111100001111000011110000', 2)
#print(ones_in_32_bit(num))

'''num = int('01010000000000000000000000000000', 2)
print(len('00010000000000000000000000000000'))
print(num)'''

test = '00001001'

def ones(eight_bit_num):
    return eight_bit_num.count("1")

#print(ones(test))

def total(min_power, bit_string):
    total = 0
    for idx, bit in enumerate(bit_string[ : : -1]):
        if bit == '1':
            total += 2**(min_power*8 + idx)
    return total

#print(total(3, test))
#print(int('00001001000000000000000000000000', 2))

def all_options():
    #what is an algorithm to generate a list of all possible
    #combinations of an 8-bit 

    bin = [[(0, 1), (0, 1), (0, 1)], [(1, 0), [1, 0], [1, 0]]]

    output = []
    for i in range(256):
        for j in range(256):
            for k in range(256):
                for l in range (256):
                    sum = bin[1][i][1] + bin[2][j][1] + bin[3][k][1]
                                       + bin[4][l][1]
                    output.append(sum)

    #***Abandoned this here - this is the same time complexity as the
    # easy solution. Need to learn bit shifting before finishing this.

    '''
    bin[0][0]- + bin[1][all]-
    bin[0][1]- + bin[1][all]-
    bin[0][2]- + bin[1][all]-

    bin[0][0 - 256][1] + bin[1][0-256][1] + bin[2][0 - 256][1]
                       + bin[3][0 - 256][1]


    
    '''
    '''output = [ (a, b, c, d) for a in bin for b in bin 
                            for c in bin for d in bin]
    sums =  [ (a + b + c + d) for a in bin for b in bin 
                            for c in bin for d in bin]'''
    sums = [bin[a][1] + bin[b][1] for a in range(b)
                                  for b in range(2)]
    print(sums)

all_options()
'''[1, 0], [1, 0], [1, 0], [1, 0]
1 + 0 + 0 + 0, 1 + 0 + 0 + 0, 1 + 1 + 0 + 0, 1 + 0 + 0 + 0'''


def fast_ones(num):
    '''
    build all possible 4-bit combinations
    '''
    bits = ['0000', '0001', '0010', '0011', '0100', '0101', 
            '0110', '0111', '1000', '1001', '1010', '1011', 
            '1100', '1101', '1110', '1111']
    bytes = [bits[i] + bits[j] for i in range(len(bits))
                               for j in range(len(bits))]
    
#Now I have a set of 256 binary strings, which represent all possible
#   8-bit strings

#I want a list with 4 sub-lists, each of which contains 256
#    sum-count tuple pairs

    master_bytes = [[(total(i, bytes[j]), ones(bytes[j]))
                        for j in range(256)]
                        for i in range(4)]
    
    print(len(master_bytes))
    print(master_bytes[1])

#Now I want all possible sums for these values
#   That will be sum( x, y, z, a for x in y for y in z for z in a for a in 256)

'''    for i in range(4):
        sum = 0
        for x in range(y):
            for y in range'''

#fast_ones(1)

'''

'''

'''    sum_table = []
    sum_counts = [sum_table[i].append((total(i, eight_bits[i][j]), ones(eight_bits[i][j])))
                                       for i in range(8)
                                       for j in range(16)]'''
'''sum_counts = [(i, (i, eight_bits[i][j]), (eight_bits[i][j])) 
                                       for i in range(8)
                                       for j in range(16)]
'''

    
    

'''
{7: [[], [], [], [], [], [], [], []], 6: [[], [], ...]...-28-24-20-16-12-8-4}
2*7 + 3

2*2*2*2




117 = 2^6 + 2^5 + 2^4 + 2^2 + 2^0
117 - 64 = 53
if 2^i < num:
count += 1, i -= 1, num = num - 2^i


7 = 2^2 + 2^0 [7 - 4, 7 - 2, 7 - 1]
5 = 4 + 1
21 = 2^4 + 2^2 + 2^0
sqrt = 4
4 = 16, rem = 5
5 = 2, rem = 1

- find sqrt of num, subtract from num
- continue until num == 0

- the rounded down sqrt will always be in it (I think)
'''