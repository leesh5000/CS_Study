'''
조합구하기 문제는 굉장히 중요!
- 이 문제를 베이스로 다른 문제들이 많이 출제됨
'''
import sys
for i in range(1,6):
    sys.stdin = open("./PS/source/in{}.txt".format(i))    
    def DFS(L, s):
        global cnt
        if L==m:
            print(" ".join(map(str, res)))
            cnt+=1
        else:
            for i in range(s, n+1):
                res[L]=i
                DFS(L+1, i+1)
    if __name__ == "__main__":
        n, m = map(int, input().split())
        res = [0] * m
        cnt = 0
        DFS(0,1)
        print(cnt)