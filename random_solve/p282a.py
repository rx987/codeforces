# https://codeforces.com/problemset/problem/282/A


def main():
    n = int(input())
    count = 0
    for _ in range(n):
        s = input()
        if "++" in s:
            count = count + 1
        elif "--" in s:
            count = count - 1
    print(count)


if __name__ == "__main__":
    main()
