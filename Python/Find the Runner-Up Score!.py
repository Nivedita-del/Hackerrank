


#Find the Runner-Up Score!


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    large=max(arr)
    for i in range(n):
        if large == max(arr):
            arr.remove(max(arr))
        maxarr=max(arr)
    print(maxarr)
