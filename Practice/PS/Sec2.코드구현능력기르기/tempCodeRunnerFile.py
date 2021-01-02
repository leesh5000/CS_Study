from filecmp import cmp

# for i in range(2):
#     with open('./PS/test_input{}.txt'.format(i+1), 'r') as f:
#         with open('./PS/my_output{}.txt'.format(i+1), 'w') as fw:
#             t = int(f.readline())
#             for j in range(t):
#                 a, b = map(int, f.readline().split())
#                 print("#%d %d" %(j+1, a+b))
            
#                 fw.write('#%d %d' %(j+1, a+b))
#                 fw.write('\n')

#             # 파일비교알고리즘
#             if cmp('./PS/my_output{}.txt'.format(i+1), './PS/test_output{}.txt'.format(i+1)):
#                 print('Test #%d: right' % (i+1))
#             else:
#                 print('Test #%d: wrong' % (i+1))