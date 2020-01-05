def merge(a, b):
    ai = 0
    bi = 0
    c = list()
    while (ai + bi) < (len(a) + len(b)):
        if ai == len(a):
            c.append(b[bi])
            bi += 1
            continue
        if bi == len(b):
            c.append(a[ai])
            ai += 1
            continue
        if b[bi] >= a[ai]:
            c.append(a[ai])
            ai += 1
        else:
            c.append(b[bi])
            bi += 1

    return c


def merge_sort(a):
    if len(a) <= 1:
        return a
    b = merge_sort(a[0: len(a)/2])      #
    c = merge_sort(a[len(a)/2: len(a)])

    return merge(b, c)


def main():
    print merge_sort([4, 5, 6, 2, 1])


main()
