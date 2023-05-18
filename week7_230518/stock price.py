def solution(prices):
    # 가격 배열의 길이
    length = len(prices)  
    # 결과를 저장할 리스트, 초기값은 모두 0
    answer = [0] * length  
    # 주식가격을 저장할 스택
    stack = []  
    # 스택이 비어있지 않고, 가격이 떨어졌을 경우
    for i in range(length):
        
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            # 가격이 떨어진 기간을 저장
            answer[j] = i - j 
        # 현재 인덱스를 스택에 추가
        stack.append(i)  

    # 스택에 남아있는 가격은 가격이 떨어지지 않은 기간이므로 처리
    while stack:
        j = stack.pop()
        # 마지막 가격까지 가격이 떨어지지 않은 기간
        answer[j] = length - j - 1  

    return answer
