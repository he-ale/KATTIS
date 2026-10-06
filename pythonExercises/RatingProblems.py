
def solve(n: int, k: int, ratings: list[float]):
    maxRatings= ((3*(n-k))+ sum(ratings))/n
    minRatings= ((-3*(n-k))+ sum(ratings))/n
    print(f"{minRatings} {maxRatings}")
    

if __name__ == "__main__":
    line= input().split(" ")
    n= int(line[0])
    k= int(line[1])
    ratings= []
    for i in range(k):
        ratings.append(float(input()))
    solve(n,k, ratings)