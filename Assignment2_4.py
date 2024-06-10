# Write a Program Which accept Number From user And return addition of factors.

def FactorsAdd(iNo2):
    iSum=0
    for i in range(1,iNo2):
        if iNo2 % i==0:
            iSum=iSum+i


  
    print("Summation of Factors is :",iSum)

def main():
    iNo1=int(input("Enter the Number : "))
    FactorsAdd(iNo1)

if __name__=="__main__":
    main()