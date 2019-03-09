"""
startip, endip,   city
1.0.1.1  1.0.1.5  NYC
1.0.1.20 1.0.1.30 SF
...
255.255.255.0  255.255.255.255  some city

question:
lookup(ip) -> city

example: lookup(1.0.1.2) -> NYC

source: google interview
"""
from bisect import bisect_left
from functools import reduce

# assume startip[n], endip[n], startip[n+1], endip[n+1] ... is increasing
records = [
    ("1.0.1.1", "1.0.1.5", "NYC"),
    ("1.0.1.20", "1.0.1.30", "SF"),
    ("1.0.1.35", "1.0.1.77", "LA"),
    ("1.0.2.0", "1.0.2.30", "CHI"),
    ("1.0.2.50", "1.0.2.90", "DA"),
]


# 2345 = 5 + 10* (4 + 10* (3 + 10* 2))
# view ip as base 2**8 integer, change ip to base 10 integer
def base256_to_base10(ip: str):
    rep = [int(i) for i in ip.split('.')]
    base = 2 ** 8
    ans = 0
    for t in rep:
        ans = ans * base + t
    return ans


# more elegant way to implement function above
def base256_to_base10_alt(ip: str):
    rep = [int(i) for i in ip.split('.')]
    base = 2 ** 8
    return reduce(lambda x, y: x * base + y, rep)


def ip_to_32binarystr(ip: str):
    def bin8(i):
        return bin(i)[2:].rjust(8, '0')

    return ''.join(bin8(int(i)) for i in ip.split('.'))


def prepare_iparr():
    return sum(((s, e) for s, e, _ in records), ())


def lookup_1(ip, iparr, conversion):
    arr = [conversion(t) for t in iparr]
    target = conversion(ip)
    index = bisect_left(arr, target)
    if index == len(iparr):
        return index, False
    else:
        is_equal = arr[index] == target
        return index, is_equal


def main():
    iparr = prepare_iparr()
    print(iparr)
    query = ("1.0.1.3", "1.0.2.10", "1.0.1.80", "1.0.22.22", "1.0.1.30", '1.0.1.77')
    ans = -1
    for q in query:
        # idx, is_equal = lookup_1(q, iparr, base256_to_base10)
        # idx, is_equal = lookup_1(q, iparr, base256_to_base10_alt)
        idx, is_equal = lookup_1(q, iparr, ip_to_32binarystr)
        print(idx, is_equal)
        if (idx % 2 == 0 and is_equal) or idx % 2 == 1:
            ans = int(idx / 2)

        if ans != -1:
            print("query {} is in city of {}".format(q, records[ans][2]))
        else:
            print("query {} not match".format(q))
        ans = -1


if __name__ == '__main__':
    main()
