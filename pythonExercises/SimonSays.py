
def solve(sentence: str):
    if sentence.startswith("Simon says"):
        print(sentence[11:])

if __name__ == "__main__":
    n= int(input())
    for i in range(n):
        sentence= input()
        solve(sentence)