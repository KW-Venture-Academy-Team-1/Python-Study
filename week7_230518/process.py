from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque([(p, i) for i, p in enumerate(priorities)])  # (중요도, 위치) 튜플을 큐에 저장
    
    while queue:
        current = queue.popleft()  # 큐에서 프로세스를 꺼냄
        if any(current[0] < p[0] for p in queue):  # 현재 프로세스보다 높은 우선순위의 프로세스가 있는지 확인
            queue.append(current)  # 있으면 현재 프로세스를 다시 큐에 넣음
        else:
            answer += 1  # 현재 프로세스를 실행
            if current[1] == location:  # 찾고자 하는 프로세스인 경우 종료
                break
    
    return answer
