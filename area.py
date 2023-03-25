def addition(a,b):
    return(a+b)
def division(sum):
    return(sum/2)
def multiplication(div,h):
    return(div*h)
a=int(input("Enter any number"))
b=int(input("Enter any number"))
h=int(input("Enter height"))
sum=addition(a,b)
div=division(sum)
area=multiplication(div,h)
print(area)