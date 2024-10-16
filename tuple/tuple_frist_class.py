'''
 # tuple 
1) it is a sequnce data type. (orederd data type)
2) it is a inmutable data type 
3) a) representation ()
   b) comma seperrated
4) it is faster the list
5) single element representation.
6) generally whenever data is fectch from database. it is stored in the form of tuple or dictionary.
7) tuple store a hetrogenise data store.
'''
fruit= ("apple", 20,100)
print(type(fruit))
print(id(fruit))
print(id(fruit[0]),id(fruit[1]),id(fruit[2]))

fruit=("aplle",20,100)
print(fruit)
fruit=("apple",20,100)+("banana",90)
print(fruit)
fruit=("apple",20,100,"banana",999)
print(fruit)
fruit=99999

print(fruit)


#fruit[2]=200 #tuple inmutable