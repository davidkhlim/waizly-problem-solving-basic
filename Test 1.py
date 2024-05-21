def miniMaxSum():
  # Input number list
  numInput = input ("Enter number :") 
  # initialize max and min values
  minNum = pow(10,9)
  maxNum = 0

  #### process input and getting the max & min sum of 4 of the 5 integers ####
  # assuming input always five space-separated integers (from the problem description)
  try:
    # process input
    numArr = numInput.strip().split(" ")
    # convert list of string to list of int and sort them ascending
    sortedNumArr = sorted([(int(i) if i!="" else 0) for i in numInput.strip().split(" ")])
    # get max and min number
    maxNum = sum(sortedNumArr[1:])
    minNum = sum(sortedNumArr[:-1])
  except ValueError as error:
    print (error)
  except:
    print("Other Errors")

  print(minNum, maxNum)

miniMaxSum()