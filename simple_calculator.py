def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  if(b!=0):
   return a/b
  else:
    print("Invalid!  Division by zero.\n")
    return None

history=[]

print("SIMPLE CALCULATOR")
print("Type 'exit' anytime you want to exit.\n")


while True:
 a=input("Enter first number: ")
 if a.lower() =="exit":
    break
 if a.lower()=="history":
   print("CALCULATION HISTORY")
   for item in history:
      print(item)
   print()
   continue
  
 a=float(a)

 op= input("Enter operator(+, -, *, /): ")
 if op.lower() =="exit":
    break

 b =input("Enter second number: ")
 if b.lower() =="exit":
    break
 b=float(b)

 if(op == "+"):
    c= add(a,b)
 elif(op == "-"):
    c= subtract(a,b)
 elif(op == "*"):
    c= multiply(a,b)
 elif(op == "/"):
     c=divide(a,b)
 else:
    print("Invalid operator, enter a valid character!\n")
    continue

 if c is not None:
  result=f"{a} {op} {b} = {c}"
  print(f"Output = {c}\n")
  history.append(result)

