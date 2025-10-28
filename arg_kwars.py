

def printer(*args):
    for n in args:
        print(n)
    
printer(1,6,8)



def calculate(n,**kwargs):        #kwargs is key value dictionary 
    n+=kwargs['add']
    print(n)

calculate(2,add=3)
