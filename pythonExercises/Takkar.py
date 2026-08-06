def solve(a: int, b: int):
    if (a > b):
        print('MAGA!')
    elif(a < b):
        print('FAKE NEWS!')
    else:
        print('WORLD WAR 3!')

if __name__ == "__main__":
    a= int(input())
    b= int(input())
    solve(a, b)