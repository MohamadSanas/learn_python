#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
import math

def add(a,b):
    return a+b
def subtract (a,b):
    return a-b
def Multiply(a,b):
    return a*b
def Divide (a,b):
    if b==0:
        print("float division by zero")
        return "None"
    return a/b
def Power(a,b):
    return pow(a,b)
def Remainder(a,b):
    return a%b

#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op (choice):
    if choice=="#":
        print("Done. Terminating")
        exit()
    elif choice=="$":
        return True
    num1=input("Enter the first number: ")
    if num1=="$":
        return True
    a=float(num1)
    
    num2=input("Enter the second number: ")
    if num2=="$":
        return True
    b=float(num2)
    
    if choice=="+":
        print  (a,choice,b," = ",add(a,b))
    elif choice=="-":
        print (a,choice,b," = ",subtract(a,b))
    elif choice=="*":
        print (a,choice,b," = ",Multiply(a,b))
    elif choice=="/":
        print (a,choice,b," = ",Divide(a,b))
    elif choice=="^":
        print (a,choice,b," = ",power(a,b))
    elif choice=="%":
        print (a,choice,b," = ",Remainder(a,b))
        
#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
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
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()