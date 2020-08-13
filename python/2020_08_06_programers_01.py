def solution(citations):
    answer = 0
    for i in range(len(citations)+1):
        cnt=0
        for j in citations:
            if i <= j:
                cnt+=1
        if cnt >= i:
            answer = i
    return answer