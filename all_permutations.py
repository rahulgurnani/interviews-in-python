def all_permutations(ls):
    if(len(ls) == 1):
        return [ls]
    res = []
    for i, a in enumerate(ls):
        permutations = all_permutations(ls[0:i] + ls[i+1:])
        for permutation in permutations:
            p = [a] + permutation
            res.append(p)

    return res


def allPermutations(ls):
    res = []
    if len(ls) == 1:
        return [ls]
    for i, a in enumerate(ls):
        permutations = allPermutations(ls[0:i] + ls[i+1:])
        for permutation in permutations:
            p = [a] + permutation
            res.append(p)
    return res


s = input("Enter a number:")
n = int(s)


ls = [i for i in range(0, n)]
all_permutation = allPermutations(ls)
end = [1, 2, 3, 4, 5, 0]
print(end in all_permutation)
