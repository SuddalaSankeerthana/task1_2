def addition(a,b):
    return(a+b)
def division(a):
    return(a/2)
def multiplication(div,h):
    return(div*h)
a=int(input("Enter any number :"))
b=int(input("Enter any number :"))
h=int(input("Enter hight:"))
sum=addition(a,b)
div=division(sum)
area=multiplication(div,h)
print(area)