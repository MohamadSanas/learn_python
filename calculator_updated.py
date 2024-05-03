history=[]

def add(a,b):
    rslt=a+b
    history.append(("{0} + {1} = {2}".format(a,b,rslt)))
    return rslt
  
def subtract(a,b):
    rslt=a-b
    history.append(("{0} - {1} = {2}".format(a,b,rslt)))
    return rslt
  
def multiply (a,b):
    rslt=a*b
    history.append(("{0} * {1} = {2}".format(a,b,rslt)))
    return rslt

def divide(a,b):
  try:
      rslt=a/b
      history.append(("{0} / {1} = {2}".format(a,b,rslt)))
      return rslt
  except Exception as e:
    history.append(("{0} / {1} = None".format(a,b)))
    print(e)
def power(a,b):
    rslt=a**b
    history.append(("{0} ^ {1} = {2}".format(a,b,rslt)))
    return rslt
  
def remainder(a,b):
    rslt=a%b
    history.append(("{0} % {1} = {2}".format(a,b,rslt)))
    return rslt
  
def select_op(choice):
  if (choice == '#'):
    return -1
  elif (choice == '$'):
    history.clear()
    return 0
 
  elif choice == '?':
      if not history:
          print("No past calculations to show")
      for entry in history:
          print(entry)
          
  elif (choice in ('+','-','*','/','^','%')):
    while (True):
      num1s = str(input("Enter first number: "))
      print(num1s)
      if num1s.endswith('$'):
        return 0
      if num1s.endswith('#'):
        return -1
        
      try:
        num1 = float(num1s)
        break
      except:
        print("Not a valid number,please enter again")
        continue
    
    while (True):
      num2s = str(input("Enter second number: "))
      print(num2s)
      if num2s.endswith('$'):
        return 0
      if num2s.endswith('#'):
        return -1
      try:  
        num2 = float(num2s)
        break
      except:
        print("Not a valid number,please enter again")
        continue
    
    result = 0.0
    last_calculation = ""
    if choice == '+':
      result = add(num1, num2)
    elif choice == '-':
      result = subtract(num1, num2)
    elif choice == '*':
      result = multiply(num1, num2)
    elif choice == '/':
      result =  divide(num1, num2)
    elif choice == '^':
      result = power(num1, num2)
    elif choice == '%':
      result = remainder(num1, num2)

    else:
      print("Something Went Wrong")
      
    last_calculation =  "{0} {1} {2} = {3}".format(num1, choice, num2, result) 
    print(last_calculation )
    
  else:
    print("Unrecognized operation")
    
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("8.History  : ? ")
  
  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()