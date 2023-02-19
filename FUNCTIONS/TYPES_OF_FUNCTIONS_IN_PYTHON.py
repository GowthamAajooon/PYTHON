# 1) NO RETURN TYPE WITHOUT ARGUMENTS
def add():
  a = int(input())
  b = int(input())
  c = a+b
  print("total",c)
add()


# 2) NO RETURN TYPE WITH ARGUMENTS
def sub(a,b):
  c = a - b
  print("Diffenece",c)
sub(10,5)


# 3) RETURN TYPE WITHOUT ARGUMENTS
def mul():
  a = 2
  b = 2
  c = a*b
  return c
print("Multiplication: ",mul())


# 4) RETURN TYPE WITH ARGUMENTS
def div(a,b):
  c = a/b
  return c
print("Division: ",div(10,5))

# 5) ARBITRARY ARGUMENT FUNCTION 
def sum(*add):
  print("a :",add[0],"\nb :",add[1])
  return add[0]+add[1]
print("Sum of a and b :",sum(10,20))

# 6) KEYWORD ARGUMENT FUNCTION
def sub(a,b):
  print("a :",a)
  print("b :",b)
  return a+b
print("difference of two's: ",sub(b=10,a=20))


# 7) ARBITRARY KEYWORD ARGUMENTS
def student(**details):
    return details
print(student(Name = 'Raja' ,Class = 12 ,Age = 20 ))

# 8) DEFAULT PARAMETER
def person(name,city="tpr"):
  print("Person name: ",name)
  print("Person city",city)
person("RAM","cbe")
person("SAM")
      
  
# 9) PASSING LIST AS AN ARGUMENT
def sumy(l):
  return sum(l)
print("Total :",sumy([1,2,3,4,5]))

# 10) RECURRSION FUNCTION

# 11) LAMBDA FUNCTION
c = lambda a:a+10
print("Passing single argument"c(10))
c = lambda a,b:a+b
print("Multiple arguments",c(10,10))


