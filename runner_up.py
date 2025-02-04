if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    runner = min(scores)
    winner = max(scores)
    for i in scores:
        if i < winner and i > runner:
            runner = i
    print(runner)
    