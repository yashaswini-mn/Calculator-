class Calculator:
    
    def addition(self, x, y):
        if(x<500 and y<500):
            print("It's easy bro can't you even do that? Let it be, I'll do it for you")
            c=x+y
            print(f"The sum is {c}")
        elif(x>500 and y>500):
            print("Well, this looks complicated! Let me do this for you")
            c=x+y
            print(f"The sum is {c}")
        else:
            print("Broo, are you out of your mind additon can be done only for numbers")
            
    def subtraction(self, x, y):
        if(x<500 and y<500):
            print("It's easy bro can't you even do that? Let it be, I'll do it for you")
            c=x-y
            print(f"The difference is {c}")
        elif(x>500 and y>500):
            print("Well, this looks complicated! Let me do this for you")
            c=x-y
            print(f"The difference is {c}")
        else:
            print("Broo, are you out of your mind subtraction can be done only for numbers")
        
        
    def multiplication(self, x, y):
        if(x<500 and y<500):
            print("It's easy bro can't you even do that? Let it be, I'll do it for you")
            c=x*y
            print(f"The product is {c}")
        elif(x>500 and y>500):
            print("Well, this looks complicated! Let me do this for you")
            c=x*y
            print(f"The product is {c}")
        else:
            print("Broo, are you out of your mind multiplication can be done only for numbers")
            
    def division(self, x, y):
        if(y==0):
            print("Brooo..!, you can't divide by zero, SIMPLE SI CHEEZ BROO!")
        if(x<500 and y<500):
            print("It's easy bro, can't you even do that? Let it be, I'll do it for you")
            c=x/y
            print(f"The divison is {c}")
        elif(x>500 and y>500):
            print("Well, this looks complicated! Let me do this for you")
            c=x/y
            print(f"The divison is {c}")
        else:
            print("Broo, are you out of your mind divison can be done only for numbers")



c=Calculator()

while True:
    print("MENU")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
        
    choice = int(input("Enter your choice babe's : "))
    if(choice==1):
        n=int(input("Enter the first number : "))
        m=int(input("Enter the second number : "))
        c.addition(n, m)
    elif(choice==2):
        n=int(input("Enter the first number : "))
        m=int(input("Enter the second number : "))
        c.subtraction(n, m)
    elif(choice==3):
        n=int(input("Enter the first number : "))
        m=int(input("Enter the second number : "))
        c.multiplication(n, m)
    elif(choice==4):
        n=int(input("Enter the first number : "))
        m=int(input("Enter the second number : "))
        c.division(n, m)
    elif(choice==5):
        break
    else:
        print("Bro please look at the menu and choose an option, your option is inavlid brooo")
            
