if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        command = input()
        ans = command.split()
        if ans[0] == 'insert':
            list.insert(int(ans[1]),int(ans[2]))
        elif ans[0] == 'print':
            print(list)
        elif ans[0] == 'remove':
            list.remove(int(ans[1]))
        elif ans[0] == 'append':
            list.append(int(ans[1]))
        elif ans[0] == 'sort':
            list.sort()
        elif ans[0] == 'pop':
            list.pop()
        elif ans[0] == 'reverse':
            list.reverse()
            