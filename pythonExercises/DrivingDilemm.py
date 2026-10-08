
def solve(S: int, D: float, T: float):
    S= S*(1609.34)/3600
    D= round(D*0.3048, 4)
    if(round((S*T),4)<D):
        print('FAILED TEST')
    else:
        print('MADE IT')

    

if __name__ == "__main__":
    S= int(input())
    D= float(input())
    T= float(input())
    solve(S, D, T)