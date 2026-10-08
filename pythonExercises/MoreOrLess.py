
def solve(a: int, b: int):
    if (a == b):
        return False
    elif (a > b):
        print('More')
        return True
    
    print('Less')
    return True

if __name__ == "__main__":
    flag= True
    while flag:
        aux= input().split(" ")
        flag= solve(int(aux[0]), int(aux[1]))