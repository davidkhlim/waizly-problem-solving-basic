from datetime import datetime

def timeConversion():
  res = None
  try:
    datetime_str = input("Enter time in 12-hour format: ")

    datetime_object = datetime.strptime(datetime_str, '%I:%M:%S%p').time()
    
    res = datetime_object
  except ValueError as e:
    print(e)
  except: 
    print("Other Error")
  finally:
    return res

print(timeConversion())