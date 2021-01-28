# import sys
# for i in range(1,5):
#     sys.stdin = open("./PS/source/in{}.txt".format(i))
#     def dfs(v):
#         if v == len(a):
#             u = []
#             v = []
#             for i in range(len(use)):
#                 if use[i]:
#                     u.append(a[i])
#                 else:
#                     v.append(a[i])
#             if sum(u) == sum(v):
#                 print("YES")
#                 sys.exit(0)
#         else:
#             use[v] = True
#             dfs(v+1)
#             use[v] = False
#             dfs(v+1)
#     if __name__ == "__main__":
#         n = int(input())
#         a = list(map(int, input().split()))
#         use = [False for _ in range(len(a))]
#         dfs(0)
#         print("NO")

def add(n):
    global a
    a += 10
if __name__ == "__main__":
    a = 10
    add(a)
    print(a)