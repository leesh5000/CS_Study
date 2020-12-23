# 십진수 기수정렬
def radix_sort(lt: list, maxElem_len: int, lt_len: int):
    # 십진수 기수 정렬이므로 버킷은 10개 필요함 (0-9까지)
    bucket_num = 10
    # 0-9까지 버킷 생성
    bucket = [[] for i in range(bucket_num)]
    # 처음은 1로 나누기
    divisor = 1

    # 리스트 안의 데이터 중 가장 긴 데이터의 길이만큼 반복
    for i in range(maxElem_len):
        # 리스트의 길이만큼 반복
        for i in range(lt_len):
            # 파이썬의 '/' 연산은 실수로 나오니까 '//'로 해줘야함
            radix = (lt[i] // divisor) % 10
            bucket[radix].append(lt[i])
        
        # 버킷에 다 넣었으면, 이제는 다시 다 꺼내서 다시 lt에 넣기
        # 버킷의 수만큼 반복하기
        idx = 0
        for i in range(bucket_num):
            # 현재 버켓의 사이즈가 0이 될때까지 다 빼서, lt에 넣기
            while(len(bucket[i])!=0):
                # 기수가 i인 버켓에 먼저들어간 놈부터 빼기 - Pop(0) = Dequeue
                lt[idx] = bucket[i].pop(0)
                idx += 1

        # divisor * 10을 해서 다음 n번째 자리의 기수를 구하기
        divisor *= 10

    
lt = [13, 212, 14, 7141, 10987, 6, 15, 6, 1, 1, 9999]
radix_sort(lt, 5, len(lt))
print(lt)