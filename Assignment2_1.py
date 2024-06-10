# create on module named as Arithamtic Which contains 4 fucations As Add() for Addition ,Sub() for substraction ,
# Mult() for multiplication,Divi() for Division All Fuctions Accepts Two PArameter As number And perform the Operation Write 
# a Python Program Which call the Fuctions From Arithamatic Module By Accepting the Parameter from user.

from Arithmetic import*
def main():

    iNo1=0
    iNo2=0
    iRet=0
    print("Enter The First Number : ")
    iNo1=(int(input()))

    print("Enter The Second  Number : ")
    iNo2=(int(input()))


    iRet=Add(iNo1,iNo2)
    print("Addition is : ",iRet)

    iRet=Sub(iNo1,iNo2)
    print("Substraction  is : ",iRet)

    iRet=Mult(iNo1,iNo2)
    print("Multiplication is : ",iRet)

    iRet=Divi(iNo1,iNo2)
    print("Division  is : ",iRet)

    
if __name__=="__main__":
    main()