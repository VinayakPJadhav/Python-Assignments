# Write A Program Which Accpet Number From USer And Return Addition  of  Digits.
def CheckeDigit(iNo2):
    count=0
    sum=0
    while(iNo2>0):
        iNo2=iNo2//10
        count=count+1
        sum=sum+count
    return sum

def main():
    iNo1=int(input("Enter the Number : "))
    
    iRet=CheckeDigit(iNo1)
    print("Addition of Digits are : ",iRet)

if __name__=="__main__":
    main()