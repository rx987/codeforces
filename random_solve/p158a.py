# https://codeforces.com/problemset/problem/158/A


def main():
    n, k = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    cutoff = arr[k - 1]
    count = 0
    for i in arr:
        if i >= cutoff and i != 0:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
