#Write a Program Which Accept on eNumber From User and Display Below Pattern.
def Pattern(iNo):
    
    for i in range(iNo):
        for j in range(iNo):
            print("*\t",end="")
        print()

def main():
    iNo1=int(input("Enter the Number : "))
    Pattern(iNo1)

if __name__=="__main__":
    main()