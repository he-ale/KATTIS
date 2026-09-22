
def solve(r:int, n: int, rooms: list[int]):
    if (r == n):
        return "too late"

    for i in range(1, r+1):
        if i not in rooms:
            return i



if __name__ == "__main__":
    rn= [int(x) for x in input().split(" ")]
    r, n= rn[0], rn[1]
    rooms= []
    for i in range(0, n):
        rooms.append(int(input()))
    print(solve(r, n, rooms))