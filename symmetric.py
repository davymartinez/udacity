# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(base_list):

    list_length = len(base_list)

    # Check if the list is square by comparing its overall length to each row's
    # length
    for row in base_list:
        if len(row) != list_length:
            return False

    # Iterate over the nested list comparing pairs of items -- a symmetric list
    # (or matrix) should be of the form list[i][j] == list[j][i]
    for i in range(list_length):
        for j in range(list_length):
            if base_list[i][j] != base_list[j][i]:
                return False

    return True

print(symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]]))
#>>> True

print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]]))
# #>>> True

print(symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]]))
#>>> False

print(symmetric([[1, 2],
                [2, 1]]))
#>>> True

print(symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]]))
#>>> False

print(symmetric([[1,2,3],
                [2,3,1]]))
#>>> False