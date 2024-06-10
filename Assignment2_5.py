# Write A program Which accpet Number From User Check Wherther number is Prime or Not.
def CheckPrime(iNo2):
    for i in range(2,int(iNo2/2+1)):
        if (iNo2 % i ) == 0:
            print("Given Number is NOT Prime ")

        else:
            print("Given Number is Prime  ")

def main():
    iNo1=int(input("Enter the Number : "))
    CheckPrime(iNo1)


if __name__=="__main__":
    main()