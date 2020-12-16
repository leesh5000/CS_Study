# class Heap:
#     def __init__(self):
#         self.arr = []
#         self.arr.append(None)

#     def move(self, inserted_idx)->bool:
#         if inserted_idx <= 1:
#             return False
        
#         parent_idx = inserted_idx // 2
#         if self.arr[inserted_idx] > self.arr[parent_idx]
#             return True
#         else:
#             return False

#     def push(self, data)->bool:        
#         self.arr.append(data)
#         inserted_idx = len(self.arr)-1

#         while self.move(inserted_idx):
#             parent_idx = int(inserted_idx/2)
#             self.arr[inserted_idx], self.arr[parent_idx] = self.arr[parent_idx], self.arr[inserted_idx]
#             inserted_idx = parent_idx

lt = [1,2,3,4,5]

if lt[8]==None:
    print('wow')
        