

def solve(G: int, T: int, N: int, w: list[int]):
    totalWeight= int((G - T)*0.9)
    weight= 0
    for i in range(N):
        weight+= w[i]
    return totalWeight-weight


if __name__ == "__main__":
    lineOne= input().split(" ")
    G, T, N= int(lineOne[0]), int(lineOne[1]), int(lineOne[2])
    w= list(map(lambda e: int(e), input().split()))
    print(solve(G, T, N, w))