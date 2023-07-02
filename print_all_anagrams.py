import itertools


def print_all_anagrams(string):
    anagrams = set(map(''.join, itertools.permutations(string)))
    print(f'Anagrams for {string} are:\n')
    cnt = 1
    for anagram in anagrams:
        print(f'#{cnt}: {anagram}')
        cnt = cnt + 1


print_all_anagrams('biro')
