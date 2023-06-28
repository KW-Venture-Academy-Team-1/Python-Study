import heapq

def solution(jobs):
    # 작업의 요청 시간을 기준으로 정렬
    jobs.sort(key=lambda x: x[0])
    n = len(jobs)  # 작업의 개수
    current_time = 0  # 현재 시간
    total_response_time = 0  # 총 응답 시간
    heap = []  # 작업을 저장할 힙
    
    while jobs or heap:
        # 현재 시간 이전에 요청된 작업이 있다면 힙에 추가
        while jobs and jobs[0][0] <= current_time:
            request_time, processing_time = jobs.pop(0)
            heapq.heappush(heap, (processing_time, request_time))
        
        if heap:
            processing_time, request_time = heapq.heappop(heap)
            current_time += processing_time
            total_response_time += current_time - request_time
        else:
            # 힙이 비어있는 경우에는 가장 먼저 요청된 작업의 시간으로 시간을 이동
            current_time = jobs[0][0]
    
    return total_response_time // n
