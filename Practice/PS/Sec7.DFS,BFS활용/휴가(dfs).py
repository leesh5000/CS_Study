import sys
for i in range(1, 6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))

    def DFS(day, budget):
        global largest
        if day > n+1:
            return
        if day == n+1:
            if budget > largest:
                largest = budget
        else:
            DFS(day+schedule[day][0], budget+schedule[day][1])
            DFS(day+1, budget)

    if __name__ == "__main__":
        n = int(input())
        schedule = [0] * (n+1)
        for i in range(1, n+1):
            t, p = map(int, input().split())
            schedule[i] = (t, p)
        largest = -2147000000
        DFS(1, 0)
        print(largest)
