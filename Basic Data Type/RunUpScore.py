if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    print(sorted(set(list(arr)))[-2])