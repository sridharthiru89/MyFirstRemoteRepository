def add(*x):
  result = 0
  for i in *x:
    result+=i
  return result
  
  if __name__=='__main__':
    print(add(5,10,15,20))
