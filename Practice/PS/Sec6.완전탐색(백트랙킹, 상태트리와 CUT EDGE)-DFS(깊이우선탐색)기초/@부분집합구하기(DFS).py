# import sys
# for i in range(1,6):
#     sys.stdin = open("./PS/source/in{}.txt".format(i))
    
#     def dfs(start, end, use):
#         if start > end:
#             for i in range(1, end+1):
#                 if use[i]:
#                     print(i, end=' ')
#             print()
#         else:
#             use[start] = True
#             dfs(start+1, end, use)
#             use[start] = False
#             dfs(start+1, end, use)        

#     if __name__ == "__main__":
#         n = int(input())
#         use = [False for _ in range(n+1)]
#         dfs(1, n, use)

lt = [1,2,3]
a,b,c = lt
print(a,b,c)