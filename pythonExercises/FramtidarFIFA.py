
def solve(n: int, k: int):
    rs= 2022 + (n // k)
    print(rs)
    return rs    

if __name__ == "__main__":
    n= int(input())
    k= int(input())
    solve(n, k)