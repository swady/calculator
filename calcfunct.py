a=int(input('enter a number '))         ##the first number
b=int(input('enter another numbr '))    ##the second number
count=1                                 ##a variable to run the loop
def add():                              ## ceating a function for addition
    d=a+b
    return(d)
def sub():                              ## ceating a function for subtraction
    d=a-b
    return(d)
def div():                              ## ceating a function for division
    d=a/b
    return(d)
def mul():                              ## ceating a function for multiplication
    d=a*b
    return(d)

while(count>0):                         ##running  a while loop for count being above 0
    op=input('enter the operations ')   ##selecting the math operation to be performed +,-,* or /
    if(op=='+'):                        ## checking the condition for addition
        print('your result ',add())
        count=0                         ## the count will become 0 and loop will terminate after the first ittration
    elif(op=='-'):
        print('your result ',sub())
        count=0
    elif(op=='/'):
        print('your result ',div())
        count=0
    elif(op=='*'):
        print('your result ',mul())
        count=0
    else:                               ##default statement if the math opetation is not matched with any given condition of if's
        print('wrong operation')        ##the loop will continue because there is no updation on count
        
