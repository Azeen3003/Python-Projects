#This function adds two numbers
def add(x,y):
    return x+y

#This function subtracts two numbers
def sub(x,y):
    return x-y

#This function multiplies two numbers
def mul(x,y):
    return x*y

#This function divides two numbers
def div(x,y):
    return x/y


print("The Calculator")
print("Menu\n 1:Add \n 2: Subtract \n 3:Multiply \n 4:Divide" )
while True:
    #Taking input from user
    choice=input("Enter your choice of operation: ")
    if choice in ('1','2','3','4'):
        try:
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))
        except ValueError:
            print("Invalid input, please input a number")
            continue
        if choice=='1':
            print(num1,'+',num2,'=',add(num1,num2))
        elif choice=='2':
            print(num1,'-',num2,'=',sub(num1,num2))
        elif choice=='3':
            print(num1,'*',num2,'=',mul(num1,num2))
        elif choice=='4':
            print(num1,'/',num2,'=',div(num1,num2))
        next=input("Perform another calculation? (Y/N):")
        if next=="N":
            break
    else:
        print("Invalid choice")
        
    
