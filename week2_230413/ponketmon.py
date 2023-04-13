# ponketmon with hash
def solution(nums):
  # create mon dictionary
  mon = {}
  
  for num in nums:
      # create new key if num doesn't exist in mon
      if num not in mon:
          mon[num] = 1
      # if num exists in mon, value+=1
      else:
          mon[num] += 1
  # The length of mon is the maximum number of different types of poncketmon.
  answer = min(len(nums)/2, len(mon))
  
  return answer
