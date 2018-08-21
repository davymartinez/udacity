#########################################################################
#                 10-row School abacus
#                         by
#                      Michael H
#########################################################################
#       Description partially extracted from from wikipedia
#
#  Around the world, abaci have been used in pre-schools and elementary
#
# In Western countries, a bead frame similar to the Russian abacus but
# with straight wires and a vertical frame has been common (see image).
# Helps schools as an aid in teaching the numeral system and arithmetic
#
#         |00000*****   |     row factor 1000000000
#         |00000*****   |     row factor 100000000
#         |00000*****   |     row factor 10000000
#         |00000*****   |     row factor 1000000
#         |00000*****   |     row factor 100000
#         |00000*****   |     row factor 10000
#         |00000*****   |     row factor 1000
#         |00000****   *|     row factor 100     * 1
#         |00000***   **|     row factor 10      * 2
#         |00000**   ***|     row factor 1       * 3
#                                        -----------
#                             Sum                123
#
# Each row represents a different row factor, starting with x1 at the
# bottom, ascending up to x1000000000 at the top row.
######################################################################

# TASK:
# Define a procedure print_abacus(integer) that takes a positive integer
# and prints a visual representation (image) of an abacus setup for a
# given positive integer value.
#
# Ranking
# 1 STAR: solved the problem!
# 2 STARS: 6 < lines <= 9
# 3 STARS: 3 < lines <= 6
# 4 STARS: 0 < lines <= 3

def print_abacus(value):
    factor = 10
    divisor = 1
    blank = '   '
    row_array = []

    while divisor < value:
        # perform mod division of the input value and then divide the result in
        # increments of 10 to "decompose" the value into its single digits,
        # which will be stored into a list -- the loop stops once the divisor
        # surpasses the input value
        row = int((value % factor) / divisor)
        factor = factor * 10
        divisor = divisor * 10
        row_array.append(row)

    while len(row_array) < 10:  # fill out the list with leading zeroes to print
        row_array.append(0)     # out the "unused" abacus rows

    row_array.reverse() # the original list gets the values input in reverse
                        # order, so we sort it back to the needed order of rows
    for i in row_array:
        # the actual abacus printing pattern:
        if i <= 5:
            print('|' + ('0' * 5) + ('*' * (5-i)) + blank + ('*' * i) + '|')
        else:
            print('|' + ('0'*(10-i)) + blank + ('0'*(i-5)) + ('*' * 5) + '|')

###  TEST CASES
print("Abacus showing 0:")
print_abacus(0)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
print("Abacus showing 12345678:")
print_abacus(12345678)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000***   **|
#>>>|00000**   ***|
#>>>|00000*   ****|
#>>>|00000   *****|
#>>>|0000   0*****|
#>>>|000   00*****|
#>>>|00   000*****|
print("Abacus showing 1337:")
print_abacus(1337)
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000*****   |
#>>>|00000****   *|
#>>>|00000**   ***|
#>>>|00000**   ***|
#>>>|000   00*****|
