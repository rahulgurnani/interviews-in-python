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


s = input("Enter a number:")
n = int(s)


ls = [i for i in range(0, n)]
all_permutation = all_permutations(ls)
print("All permutations:")
print(all_permutation)
