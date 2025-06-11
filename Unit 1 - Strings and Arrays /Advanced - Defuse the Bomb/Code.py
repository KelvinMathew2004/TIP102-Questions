def defuse(code, k):
  res = [0] * len(code)
  length = len(code)
    
  if k > 0:
    left = 0
    sum = 0
    for right in range(length+k):
      sum = sum + code[right % length]
      if right - left == k:
        res[left % length] = sum - code[left % length]
        sum = sum - code[left % length]
        left +=1
  elif k < 0:
    left = 0
    sum = 0
    for right in range(length+abs(k)):
      sum = sum + code[right % length]
      if right - left == abs(k):
        res[right % length] = sum - code[right % length]
        sum = sum - code[left % length]
        left +=1

  return res