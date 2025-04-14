def sleep_in(weekday, vacation):
  if weekday == False and vacation == False:
    print(True)
  elif weekday == True and vacation == False:
      print(False)
  elif weekday == False and vacation == True:
      print(True)
  
weekday = input("Enter true or false: ")
vacation = input("Enter true or false: ")

print(sleep_in(weekday, vacation))