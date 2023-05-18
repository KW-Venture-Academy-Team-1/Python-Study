def solution(s):
    stack = []
    for ch in s:
        # '('를 만나면 stack에 추가
        if ch == '(':
            stack.append(ch)
        # ')'를 만나면 stack에서 뺌
        elif ch == ')':
            # stack에 문자가 더이상 겂거나, top이 '('이 아닌 경우, False
            if len(stack) == 0 or stack[-1] != '(':
                return False
            # stack의 top을 제거
            stack.pop()
    # 다 빼냈는데 stack에 문자가 남아있는 경우. False
    if len(stack) > 0:
        return False
    return True
