from collections import namedtuple
thistuple=(1,2,"aditya")
print(type(thistuple))


thisisnottuple=(1)   #   thisisnottuple=(1,)  this will be a tuple
print(type(thisisnottuple))


print(thistuple[0])

#thistuple[0]=3     , tuples are immutable , cant assign value to it 


#namedtuple


Color=namedtuple('Color',['red','green','blue'])

white=Color(255,255,255)


print(type(Color))

print(white.red)
