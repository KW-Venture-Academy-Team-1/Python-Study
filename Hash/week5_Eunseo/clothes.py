def solution(clothes):
    hash_map = {}
    #옷의 종류를 key, 그 수를 value로 해시테이블 구성
    for name, kind in clothes:
        if kind in hash_map:
            hash_map[kind] += 1
        else:
            hash_map[kind] = 1
    
    answer = 1
    #옷을 조합하는 경우의 수(입는다or안입는다)
    for value in hash_map.values():
        answer *= (value + 1)
        
    #옷을 모두 안입는 경우 뺀다
    return answer - 1
