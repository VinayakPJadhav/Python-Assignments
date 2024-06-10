# Write a Program  which Accept Number From user and  return its factorial.


def Factorial(iNo2):
    ifact=1
    for i in range(1,iNo2+1):
        
        ifact= ifact * i
    print("The Factorial is : " ,ifact)


def main():
    iNo1=int(input("Enter teh Number : "))
    Factorial(iNo1)

if __name__=="__main__":
    main()
