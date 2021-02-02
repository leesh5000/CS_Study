import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def DFS(L, score, time):
        global largest
        if time > m:
            return
        if L == n:
            if score > largest:
                largest = score
        else:
            DFS(L+1, score+scores[L], time+times[L])
            DFS(L+1, score, time)

    if __name__ == "__main__":
        n, m = map(int, input().split())
        scores = []
        times = []
        for _ in range(n):
            score, time = map(int, input().split())
            scores.append(score)
            times.append(time)
        largest = 0
        DFS(0, 0, 0)
        print(largest)
