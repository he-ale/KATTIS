
def solve(n: int):
    rs= '+' + '-'*n + '+'
    for i in range(0, n):
        rs= rs + '\n' + '|' + ' '*n + '|'

    rs= rs+ '\n+' + '-'*n + '+'
    return rs

if __name__ == "__main__":
    n= int(input())

    print(solve(n))