
def solve(n: int, s: str):
    ans = 0
    if "lv" in s:
        ans= 0
    elif "l" in s or "v" in s:
        ans= 1
    else:
        ans= 2

    print(ans)

if __name__ == "__main__":
    n = int(input())
    s = input().strip()
    solve(n, s)