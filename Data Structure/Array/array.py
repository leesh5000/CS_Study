array = [1,2,3,4,5]
print(array)

array_2d = [[1,2,3],[4,5,6],[7,8,9]]
print(array_2d[0])
print(array_2d[0][1])

# Ex1.
dataset = ['Bymm Mom', 'Hello Mom', 'Modern', 'Who','Wow']

m_count = 0
for d in dataset:
    for i in d:
        if i=='m' or i=='M':
            m_count+=1

print(m_count)

