# from filecmp import cmp

# # in{}의 개수만큼 for문
# for q in range(1,6):
#     with open('./PS/in{}.txt'.format(q), 'r') as f1:
#         with open('./PS/my_out{}.txt'.format(q), 'w') as f2:
#             """ solution """
#             n, m = map(int, f1.readline().split())
#             lt = list(map(int, f1.readline().split()))
            
#             ans_set = set()
#             for i in range(len(lt)-2):
#                 for j in range(i+1, len(lt)-1):
#                     for k in range(j+1, len(lt)):
#                         s = lt[i] + lt[j] + lt[k]
#                         ans_set.add(s)

#             ans_lt = list(ans_set)
#             ans_lt.sort(reverse=True)
#             print(ans_lt[m-1])

#             """ file write """
#             f2.write("%d" % ans_lt[m-1])

#         """ file comparison """
#         if cmp('./PS/my_out{}.txt'.format(q), './PS/out{}.txt'.format(q)):
#             print('Test #%d: right' % (q))
#         else:
#             print('Test #%d: wrong' % (q))

f1 = open('./PS/source/out1.txt')
print(f1.readline())
