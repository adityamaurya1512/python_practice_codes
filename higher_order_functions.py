

def add(a,b):
    return a+b

def calculate(a,b,func):
    return func(a,b)

sum=calculate(2,3,add)
print(sum)

