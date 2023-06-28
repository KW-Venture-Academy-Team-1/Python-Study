import heapq

def solution(operations):
    max_heap = []  # 최댓값을 추적하기 위한 우선 순위 큐
    min_heap = []  # 최솟값을 추적하기 위한 우선 순위 큐
    
    for operation in operations:
        op, num = operation.split()
        num = int(num)
    
        if op == "I":
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        elif op == "D":
            if not max_heap:
                continue
            
            if num == 1:
                max_val = heapq.heappop(max_heap)
                min_heap.remove(-max_val)
            elif num == -1:
                min_val = heapq.heappop(min_heap)
                max_heap.remove(-min_val)
    
    if not max_heap:
        return [0, 0]
    
    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
