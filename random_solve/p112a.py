# https://codeforces.com/problemset/problem/112/A


def main():
    s = input().lower()
    t = input().lower()

    if s == t:
        print(0)
    elif s > t:
        print(1)
    else:
        print(-1)


if __name__ == "__main__":
    main()
