from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 다리를 나타내는 데크 초기화
    bridge = deque([0] * bridge_length) 
    # 현재 다리 위의 트럭 무게 합계
    total_weight = 0  
    # 대기중인 트럭들을 데크로 변환
    truck_weights = deque(truck_weights)  

    while truck_weights:
      # 가장 앞에 있는 트럭을 다리에서 제거
        total_weight -= bridge.popleft()  
        # 다리에 새로운 트럭이 올라갈 수 있는지 확인
        if total_weight + truck_weights[0] <= weight: 
          # 대기중인 트럭에서 트럭을 꺼내 다리에 올림
            truck = truck_weights.popleft()  
            bridge.append(truck)
            total_weight += truck
        else:
          # 다리 위에 트럭이 올라갈 수 없으면 0을 추가하여 시간 경과를 표현
            bridge.append(0)  
        answer += 1
   # 마지막 트럭이 다리를 완전히 건너는 시간 추가
    answer += bridge_length 
    return answer
