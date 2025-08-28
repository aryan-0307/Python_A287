print("hello world")

age=30
Age=20

print(age)
print(Age)

a=b=c=20
# camel case
myNameIs="Aryan"
# Snake case
My_Name_Is="Dixit"
# pascal case

print(myNameIs)
print(My_Name_Is)


#unpack collection
# A collection of values in a list , tuple ect Python allows yout to extract values 
fruits=["Apple","banana","Cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)


#global variable without keyword

x="awesome"
def myFunct():
   print("python is "+x)
myFunct()

#with global keyword

def myFunc():
   global x
x="fantastic"

myFunc()


print("python is always  "+x)


var1 = 1
var2 = True
var3 = 18.023
var4 = 10+3j
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4)) 
