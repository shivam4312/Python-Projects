import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for excersise \nEnter 2 for food\n"))
        if(c==1):
            value=input("type here\n")
            with open("shivam-ex.txt","a") as op:
                op.write(str([str(gettime())])+": " + value +"\n")
            print("successfully written")
        elif(c==2):
            value= input("type here\n")
            with open("shivam-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("Enter 1 for excersise \nEnter 2 for food\n"))
        if (c == 1):
            value = input("type here\n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("Enter 1 for excersise \nEnter 2 for food \n"))
        if (c == 1):
            value = input("type here\n")
            with open("Abhishek-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("Abhishek-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz Enter valid input (1(shivam),2(rohan),3(Abhishek)")
def retrieve(k):
    if k==1:
        c=int(input("Enter 1 for excersise \nEnter 2 for food\n"))
        if(c==1):
            with open("shivam-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("shivam-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("Enter 1 for excersise \nEnter 2 for food\n"))
        if (c == 1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("Enter 1 for excersise \nEnter 2 for food\n"))
        if (c == 1):
            with open("Abhishek-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("Abhishek-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz Enter valid input (shivam,rohan,Abhishek)")
print("health management system: ")
a=int(input("press 1 for log the value \npress 2 for retrieve \n "))

if a==1:
    b = int(input("press 1 for shivam \npress 2 for rohan \npress 3 for Abhishek \n "))
    take(b)
else:
    b = int(input("press 1 for shivam \npress 2 for rohan \npress 3 for Abhishek \n"))
    retrieve(b)

