# http://codeforces.com/problemset/problem/1/A

import math


def main():
    n, m, a = map(int, input().split(" "))
    res = math.ceil(m/a) * math.ceil(n/a)
    print(res)


if __name__ == "__main__":
    main()
