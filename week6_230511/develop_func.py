from collections import deque

def solution(progresses, speeds):
    left=[]
    # p는 progressesm, s는 speeds
    for p, s in zip(progresses, speeds):
        # 남은 작업량/속도=남은 일 수
        days = (100 - p) // s
        # 나머지가 있는 경우 남은 일 수 +1
        if (100 - p) % s > 0:
            days += 1
        left.append(days)
    
    answer = []
    # 큐에다가 left 넣음
    queue = deque(left)
    while queue:
        cnt = 1
        # 맨 앞의 progresses를 꺼냄
        day = queue.popleft()
        # day>=queue[0]이면 queue에서 빼내고, cnt를 1 증가시켜 줘서 day가 완료되어 배포되었을 때
        # cnt만큼 한 번에 배포되도록 함 
        while queue and queue[0] <= day:
            queue.popleft()
            cnt += 1
        answer.append(cnt)
    return answer
