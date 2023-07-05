def add(num1,num2):
    sum=int(num1+num2)
    print(sum)

def mul(num1,num2):
    multi=int(num1*num2)
    print(multi)  

def div(num1,num2):
    division=int(num1/num2)
    print(division)

def sub(num1,num2):
    substraction=int(num1-num2)
    print(substraction)


num1=int(input("Enter first number: "))
operator=input("Enter an operator: ")
num2=int(input("Enter second number: "))

def calculator(num1, operator, num2):
    if operator=="+":
        add(num1,num2)
    elif operator=="-":
        sub(num1,num2)    
    elif operator=="*":
        mul(num1,num2)
    elif operator=="/":
        div(num1,num2)
    else:
        print("Enter a correct operator")


calculator(num1, operator, num2)


# if operator=="+":
#     add(num1,num2)
# elif operator=="-":
#     sub(num1,num2)    
# elif operator=="*":
#     mul(num1,num2)
# elif operator=="/":
#     div(num1,num2)
# else:
#     print("Enter a correct operator")






            

