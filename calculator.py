num1=float(input("Enter Number1: "))
operator=input(" ")
num2=float(input("Enter Number2: "))

if (operator=='+'):
  ans=num1+num2
  print("The solution is: ",ans)
while(operator=='-'):
  if(num1>num2):
    ans=num1-num2
    print("The solution is: ",ans)
  if(num2>num1):
    ans=num2-num1
    print("The solution is: ",ans)
    break
if(operator=='*'):
  ans=num1*num2
  print("The solution is: ",ans)
while(operator=='/'):
  if(num1>num2):
    ans=num1/num2
    print("The solution is: ",ans)
  if(num2>num1):
    ans=num2/num1
    print("The solution is: ",ans)
    break
