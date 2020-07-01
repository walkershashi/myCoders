def stackTheCubes(sideLengths):
    i = 0
    
    while i < len(sideLengths) - 1 and sideLengths[i] >= sideLengths[i+1]:
        i += 1
    while i <len(sideLengths) - 1 and sideLengths[i] <= sideLengths[i+1]:
        i += 1
    
    return ("Yes" if i == len(sideLengths) - 1 else "No")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        sideLen = list(map(int, input().split()))
        res = stackTheCubes(sideLen)
        print(res)