# https://codeforces.com/problemset/problem/71/A


def main():
    n = int(input())
    for _ in range(n):
        s = input()
        if len(s) <= 10:
            print(s)
        else:
            print(s[0] + str(len(s) - 2) + s[len(s) - 1])


if __name__ == "__main__":
    main()
