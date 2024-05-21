def plusMinus():
  n = (input("Size of array (optional): "))
  # 1. trim whitespace at the beginning and the end
  # 2. split the string by ' '
  # 3. filter out empty strings
  # 4. convert each element to int
  arr = list(map(int, filter(lambda x: x != "",input("Enter array elements: ").strip().split(' '))))
  arrLen = len(arr)
  
  if n != "":
    if int(n) != arrLen:
      raise BaseException("Invalid array size")
    
  posArrLen = len(list(filter(lambda x: x > 0, arr)))
  negArrLen = len(list(filter(lambda x: x < 0, arr)))
  zeroArrLen = len(list(filter(lambda x: x == 0, arr)))
  print(f"{posArrLen/arrLen:0,.6f}")
  print(f"{negArrLen/arrLen:0,.6f}")
  print(f"{zeroArrLen/arrLen:0,.6f}")

plusMinus()