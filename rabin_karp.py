import string

PRIME = 1000000007


def to_dec(c):
    return (ord(c) - ord('a'))


def search(pat, text):
    # compute hash first
    k = len(pat)
    hashes = list()
    multiply = 1
    hash = 0
    pat_hash = 0
    for i in reversed(range(0, k)):
        hash += to_dec(text[i]) * multiply
        hash = hash % PRIME
        pat_hash = (pat_hash + to_dec(pat[i]) * multiply) % PRIME
        multiply = (multiply * 26) % PRIME

    hashes.append(hash)
    for i in range(k, len(text)):
        hashes.append((
            (hashes[i - k] - (to_dec(text[i-k]) * 26**(k-1)) + PRIME)*26
            + to_dec(text[i])) % PRIME)

    print(hashes)
    print(pat_hash)


search('aab', 'baabaabaaaaaaab')
