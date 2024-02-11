# https://codeforces.com/problemset/problem/339/A

def main():
    items = input().split('+')
    items.sort()
    res = '+'.join(items)
    print(res)

if __name__ == '__main__':
    main()