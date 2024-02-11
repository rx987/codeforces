# https://codeforces.com/problemset/problem/231/A


def main():
    n = int(input())
    count = 0
    for _ in range(n):
        a, b, c = map(int, input().split(" "))
        res = [a, b, c]
        filterd = len(list(filter(lambda x: x == 1, res)))
        if filterd >= 2:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
