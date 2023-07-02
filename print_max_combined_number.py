import itertools


def find_max_combined_number(permutations):
    maxCombinedNumber = ""
    for permutation in permutations:
        combinedNumber = "".join(map(str, permutation))
        if (combinedNumber > maxCombinedNumber):
            maxCombinedNumber = combinedNumber
    return maxCombinedNumber


def print_max_combined_number(array):
    permutations = itertools.permutations(array)
    print(
        f'Max. combined number of {array} is {find_max_combined_number(permutations)}'
    )


print_max_combined_number([50, 2, 1, 9])
print_max_combined_number([5, 50, 56])
print_max_combined_number([420, 42, 423])
