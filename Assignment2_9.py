# Write A Program Which Accpet Number From USer And Returnit Digits.
def CheckeDigit(iNo2):
    count=0
    while(iNo2>0):
        iNo2=iNo2//10
        count=count+1
    return count

def main():
    iNo1=int(input("Enter the Number : "))
    
    iRet=CheckeDigit(iNo1)
    print("total Number of Digits are : ",iRet)

if __name__=="__main__":
    main()