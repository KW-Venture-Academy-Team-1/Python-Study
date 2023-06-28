import heapq

def solution(scoville, K):
    answer = 0
    # 주어진 리스트를 최소 힙으로 변환
    heapq.heapify(scoville)  
    
    while scoville[0] < K:
        # 음식이 2개 이상 없을 경우 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없음
        if len(scoville) < 2:  
            return -1
        
        # 가장 맵지 않은 음식과 두 번째로 맵지 않은 음식을 섞어 새로운 음식 생성
        mixed_food = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mixed_food)
        
        answer += 1
    
    return answer
