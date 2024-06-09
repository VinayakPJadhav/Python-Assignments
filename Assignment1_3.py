# Write a program which contains one function named as Add() which accepts two Number
# from user and return addtion of that two number  

def Add(iValue1,iValue2):
    Ans=iValue1+iValue2
    return Ans

def main():

    
    print("Enter First number :")
    iNo1=int(input())
    print("Enter second Number :")
    iNo2=int(input())
    
    
    iSum=Add(iNo1,iNo2)
    print("Addition of two number is :",iSum)

if __name__ =="__main__":
    main()
