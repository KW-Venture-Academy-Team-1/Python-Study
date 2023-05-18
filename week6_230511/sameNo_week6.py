def solution(arr):
    # 스택 초기화
    stack = [arr[0]]
    # arr의 길이만큼 반복
    for i in range(1, len(arr)):
        # stack의 마지막에 있는 원소와 arr의 원소가 서로 다르면 stack에 넣음
        if stack[-1]==arr[i]:
            continue
        else:
            stack.append(arr[i])
            
    return stack
